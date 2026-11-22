#!/usr/bin/env python3
"""Search actual wiki paragraphs; output paths and cited source records."""
import argparse, json, re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(); p.add_argument('query'); args=p.parse_args()
terms={t for t in re.findall(r'[a-z0-9]+',args.query.lower()) if len(t)>1}-{'what','is','the','how','does','can','using','of','as','an','a','are','be','in','and','to'}
results=[]
for path in (R/'wiki').rglob('*.md'):
 text=path.read_text(); title=text.splitlines()[0].lower(); hay=text.lower()
 score=sum(3*bool(re.search(r'\b'+re.escape(term)+r'\b', title))+bool(re.search(r'\b'+re.escape(term)+r'\b', hay)) for term in terms)
 if path.name == 'index.md': score //= 3
 if score: results.append((score,path,text))
sources={s['id']:s for s in json.loads((R/'raw/sources.json').read_text())}
for score,path,text in sorted(results,key=lambda x:-x[0])[:5]:
 print(f'\n--- {path.relative_to(R)} (score {score}; 待審) ---\n{text}')
 for sid in sorted(set(re.findall(r'\bS0[1-6]\b',text))):
  s=sources[sid]; print(f"{sid}: {s['url']} — {s['locator']}")
if not results: print('找不到匹配頁面；不要用外部知識補造答案。')
