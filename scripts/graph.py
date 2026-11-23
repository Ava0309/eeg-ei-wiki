#!/usr/bin/env python3
"""Run automated gates, recording real failures; humans perform reviews and repairs."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import uuid

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / 'reports' / 'workflow-runs'
MANIFEST = ROOT / 'reports' / 'n8-scoped-decision.json'
MAX_FAILURES = 3


def snapshot_inputs():
    """Ensure the explicitly reviewed files still match the human decision."""
    try:
        decision = json.loads(MANIFEST.read_text())
        if decision.get('decision') != 'SCOPED_PASS' or not decision.get('sha256'):
            return False, 'N8 scoped decision missing or not approved'
        expected_concepts = {str(p.relative_to(ROOT)) for p in (ROOT / 'wiki' / 'concepts').glob('*.md')}
        recorded_concepts = {p for p in decision['sha256'] if p.startswith('wiki/concepts/') and p.endswith('.md')}
        changed = sorted(expected_concepts ^ recorded_concepts)
        for name, expected in decision['sha256'].items():
            path = ROOT / name
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
                changed.append(name)
        if changed:
            return False, 'N8 review inputs missing or changed: ' + ', '.join(changed)
        return True, 'SCOPED_PASS (human review; matching reviewed input snapshot)'
    except (OSError, ValueError, KeyError) as exc:
        return False, f'N8 decision unavailable: {exc}'


def missing_sources():
    try:
        sources = json.loads((ROOT / 'raw/sources.json').read_text())
        if len(sources) != 6:
            return f'expected six source records; found {len(sources)}'
        missing = [s.get('id', '?') for s in sources
                   if s.get('access') != 'FULL_ACCESS' or s.get('ingest') != 'PASS'
                   or not s.get('url') or not (ROOT / 'wiki' / 'papers' / (s.get('id', '') + '.md')).is_file()]
        return 'source/ingest unavailable: ' + ', '.join(missing) if missing else None
    except (OSError, ValueError, TypeError) as exc:
        return f'source registry unavailable: {exc}'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--resume', metavar='STATE', help='resume an unresolved loop from its state.json')
    args = parser.parse_args()
    previous = None
    if args.resume:
        try:
            previous = json.loads(Path(args.resume).read_text())
            if previous['overall'] != 'LOCAL_REPAIR':
                parser.error('only a LOCAL_REPAIR state can be resumed; STOP requires a new authorized workflow')
        except (OSError, ValueError, KeyError) as exc:
            parser.error(f'cannot read previous state: {exc}')
    stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    run_id = stamp + '-' + uuid.uuid4().hex[:8]
    run_dir = RUNS / run_id
    run_dir.mkdir(parents=True)
    failures = dict(previous.get('failure_counts', {})) if previous else {}
    state = {'run_id': run_id, 'previous_state': args.resume if args.resume else None,
             'failure_counts': failures, 'checks': [], 'overall': None,
             'note': 'Automated checks do not perform or certify scientific review; repair is manual.'}
    env = os.environ.copy()
    env['SCREENSHOT_DIR'] = str(run_dir / 'screenshots')
    stages = [
        ('N4', 'Wiki lint', [sys.executable, 'scripts/check.py'], 'N1/N3'),
        ('N6/N9', 'Evidence map and HTML structure', [sys.executable, 'scripts/check_deck.py'], 'N6/N7/N9'),
        ('N7/N9', 'Teaching mathematics', ['node', 'tests/teaching_math.cjs'], 'N7/N9'),
        ('N8', 'Independent scientific review snapshot', None, 'N6/N7/N8'),
        ('N9', 'Rendered graph', ['node', 'tests/render_plot.cjs'], 'N9'),
        ('N10', 'Desktop and mobile browser', ['node', 'tests/browser.cjs'], 'N9/N7'),
    ]
    source_problem = missing_sources()
    state['source_preflight'] = {'node': 'N1', 'result': 'BLOCKED' if source_problem else 'PASS',
                                 'reason': source_problem, 'scope': 'registry and paper notes only; no network or semantic verification'}
    if source_problem:
        state['checks'].append({'node': 'N1', 'check': 'Source availability records', 'result': 'BLOCKED',
                                'reason': source_problem, 'return_to': 'N1', 'attempt': 0})
        state.update(overall='STOP', stop_reason='SOURCE_MISSING', next='Stop; obtain source and record evidence')
    else:
        for node, label, command, back in stages:
            key = node + ':' + label
            attempt = failures.get(key, 0) + 1
            log_name = f'{len(state["checks"])+1:02d}-{node.replace("/", "-")}.log'
            result, reason, code = 'PASS', '', 0
            if command is None:
                ok, reason = snapshot_inputs()
                result = 'SCOPED_PASS' if ok else 'BLOCKED'
            elif not shutil.which(command[0]):
                result, reason, code = 'BLOCKED', f'missing executable: {command[0]}', None
            else:
                try:
                    proc = subprocess.run(command, cwd=ROOT, env=env, text=True,
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)
                    code, reason = proc.returncode, proc.stdout
                    if code:
                        result = 'FAIL'
                except (OSError, subprocess.TimeoutExpired) as exc:
                    result, reason, code = 'BLOCKED', str(exc), None
            (run_dir / log_name).write_text(reason or 'PASS\n')
            entry = {'node': node, 'check': label, 'result': result, 'attempt': attempt,
                     'return_to': back if result in ('FAIL', 'BLOCKED') else None,
                     'exit_code': code, 'reason': reason.strip() if result in ('FAIL', 'BLOCKED') else None,
                     'log': str((run_dir / log_name).relative_to(ROOT))}
            state['checks'].append(entry)
            print(f'{node}: {label}: {result}', flush=True)
            if result in ('FAIL', 'BLOCKED'):
                if result == 'FAIL':
                    failures[key] = attempt
                stop = result == 'BLOCKED' or attempt >= MAX_FAILURES
                state.update(overall='STOP' if stop else 'LOCAL_REPAIR',
                             stop_reason=('BLOCKED' if result == 'BLOCKED' else 'RETRY_LIMIT') if stop else None,
                             next=('Stop; resolve missing dependency or review' if result == 'BLOCKED'
                                   else 'Stop; retry limit reached' if stop
                                   else f'Human/agent repair at {back}; resume using this state'))
                break
        else:
            state.update(overall='AUTOMATED_GATES_PASS', stop_reason=None,
                         next='Review manual nodes and complete delivery')
    state_path = run_dir / 'state.json'
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
    print(f'{state["overall"]}; state: {state_path.relative_to(ROOT)}')
    return 0 if state['overall'] == 'AUTOMATED_GATES_PASS' else 1


if __name__ == '__main__':
    sys.exit(main())
