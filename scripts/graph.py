#!/usr/bin/env python3
"""Run implemented gates in order; failures return to local owner, maximum 3 tries."""
import argparse,json,subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1];p=argparse.ArgumentParser();p.add_argument('--attempt',type=int,default=1);a=p.parse_args()
if not 1<=a.attempt<=3: print('STOP: local retry limit is three');sys.exit(2)
stages=[('N4 Wiki lint','scripts/check.py','N1/N3'),('N6 Evidence map / N9 HTML structure','scripts/check_deck.py','N6/N7/N9')]
for node,script,back in stages:
 print('\n'+node,flush=True);r=subprocess.run([sys.executable,str(R/script)],cwd=R)
 if r.returncode:
  state={'node':node,'result':'FAIL','return_to':back,'attempt':a.attempt,'next':'STOP' if a.attempt==3 else 'LOCAL_REPAIR'};break
else:state={'node':'N9 HTML structure','result':'PASS','next':'N8 independent review and N10 browser QA','attempt':a.attempt,'note':'Programmatic gates do not certify semantic claims or browser behavior.'}
(R/'reports/graph-state.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n');print(json.dumps(state,ensure_ascii=False));sys.exit(state['result']!='PASS')
