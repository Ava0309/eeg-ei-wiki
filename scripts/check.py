#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]; issues=[]
sources=json.loads((R/'raw/sources.json').read_text()); ids=[s['id'] for s in sources]
def check(ok,msg):
 print(('PASS' if ok else 'FAIL')+' '+msg)
 if not ok: issues.append(msg)
check(len(ids)==len(set(ids)),'source IDs unique')
check(all(re.fullmatch(r'10\.\d{4,9}/\S+',s['doi']) for s in sources),'DOI syntax (not network validation)')
check(sum(s['ingest']=='PASS' and s['access']=='FULL_ACCESS' for s in sources)>=5,'at least five completed full-text ingests')
for p in (R/'wiki').rglob('*.md'):
 t=p.read_text()
 for sid in set(re.findall(r'\bS\d\d\b',t)):
  if sid not in ids: issues.append(f'{p.relative_to(R)} unknown {sid}')
 for link in re.findall(r'\]\(([^)]+)\)',t):
  if not re.match(r'\w+://',link) and not link.startswith('#') and not (p.parent/link.split('#')[0]).exists(): issues.append(f'{p.relative_to(R)} broken {link}')
check(not issues or all(x=='at least five completed full-text ingests' for x in issues),'wiki source IDs and links resolve')
check((R/'slides/evidence-map.json').exists(),'evidence map exists')
print(f'Issues: {len(issues)}'); sys.exit(bool(issues))
