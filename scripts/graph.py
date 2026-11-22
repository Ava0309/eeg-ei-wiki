#!/usr/bin/env python3
"""Gate the workflow: do not create slides if prerequisites fail."""
import json, subprocess, sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=subprocess.run([sys.executable,str(R/'scripts/check.py')],cwd=R)
status={'node':'N4 wiki lint','result':'PASS' if p.returncode==0 else 'FAIL','next':'N5 retrieval' if p.returncode==0 else 'N1 source ingest / N3 wiki integration','retries':0,'note':'No automatic repair; operator must resolve failed conditions, maximum three local attempts.'}
(R/'reports/graph-state.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(status,ensure_ascii=False)); sys.exit(p.returncode)
