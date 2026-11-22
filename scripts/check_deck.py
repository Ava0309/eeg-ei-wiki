#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
from html.parser import HTMLParser
R=Path(__file__).resolve().parents[1]; errors=[]
S={x['id']:x for x in json.loads((R/'raw/sources.json').read_text())}; p=R/'slides/evidence-map.json'
if not p.exists():print('FAIL missing evidence map');sys.exit(1)
m=json.loads(p.read_text());print('Slides:',len(m))
if not 8<=len(m)<=15:errors.append('slide count')
for s in m:
 for k in ('id','learning_objective','wiki_page','source_ids','source_locator','exact_claim','title','body'):
  if not s.get(k):errors.append(s.get('id','?')+' missing '+k)
 if not (R/s['wiki_page']).exists():errors.append(s['id']+' wiki missing')
 for sid in s['source_ids']:
  if sid not in S or S[sid]['ingest']!='PASS':errors.append(s['id']+' source not ingested '+sid)
page=(R/'index.html').read_text() if (R/'index.html').exists() else ''
for s in m:
 if f'data-id="{s["id"]}"' not in page or s['body'] not in page:errors.append(s['id']+' HTML differs from mapped content')
for token in ('id="freq"','id="beta"','ArrowLeft','ArrowRight','Synthetic Data'):
 if token not in page:errors.append('missing '+token)
print('PASS evidence and HTML structure' if not errors else 'FAIL '+str(errors));sys.exit(bool(errors))
