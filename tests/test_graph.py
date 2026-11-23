"""Isolated loop state tests; simulated failures never enter project records."""
import importlib.util
import json
from pathlib import Path
from unittest import TestCase, main
from unittest.mock import patch
from tempfile import TemporaryDirectory
from types import SimpleNamespace

SPEC = importlib.util.spec_from_file_location('graph', Path(__file__).resolve().parents[1] / 'scripts/graph.py')
graph = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(graph)


class LoopTests(TestCase):
    def test_three_failures_stop_and_preserve_history(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            runs = root / 'runs'
            proc = SimpleNamespace(returncode=1, stdout='simulated failure for isolated test')
            with patch.object(graph, 'ROOT', root), patch.object(graph, 'RUNS', runs), \
                 patch.object(graph, 'missing_sources', return_value=None), \
                 patch.object(graph.shutil, 'which', return_value='/test/python'), \
                 patch.object(graph.subprocess, 'run', return_value=proc):
                previous = None
                for number in range(1, 4):
                    argv = ['graph.py'] + (['--resume', str(previous)] if previous else [])
                    with patch('sys.argv', argv):
                        self.assertEqual(graph.main(), 1)
                    files = sorted(runs.glob('*/state.json'), key=lambda p: p.stat().st_mtime_ns)
                    previous = files[-1]
                    state = json.loads(previous.read_text())
                    self.assertEqual(state['checks'][0]['attempt'], number)
                    self.assertEqual(state['overall'], 'STOP' if number == 3 else 'LOCAL_REPAIR')
                self.assertEqual(len(files), 3)
                self.assertEqual(state['stop_reason'], 'RETRY_LIMIT')

    def test_missing_source_stops_without_running_checks(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(graph, 'ROOT', root), patch.object(graph, 'RUNS', root / 'runs'), \
                 patch.object(graph, 'missing_sources', return_value='source absent'), \
                 patch.object(graph.subprocess, 'run') as run, patch('sys.argv', ['graph.py']):
                self.assertEqual(graph.main(), 1)
                run.assert_not_called()
                state = json.loads(next((root / 'runs').glob('*/state.json')).read_text())
                self.assertEqual(state['stop_reason'], 'SOURCE_MISSING')
                self.assertEqual(state['checks'][0]['result'], 'BLOCKED')


if __name__ == '__main__':
    main()
