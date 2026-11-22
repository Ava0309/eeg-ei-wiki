#!/usr/bin/env python3
"""Render canonical, source-mapped slide content; visual code is kept separately."""
import json, html
from pathlib import Path
R=Path(__file__).resolve().parents[1]
slides=json.loads((R/'slides/evidence-map.json').read_text())
sources={x['id']:x for x in json.loads((R/'raw/sources.json').read_text())}
blocks=[]
for s in slides:
 links=' · '.join(f'<a href="{html.escape(sources[i]["url"],quote=True)}" target="_blank" rel="noopener">{i}</a>' for i in s['source_ids'])
 wiki='https://github.com/Ava0309/eeg-ei-wiki/blob/main/'+s['wiki_page']
 blocks.append(f'''<section class="slide" id="slide-{s['id']}" data-id="{s['id']}" hidden>
 <div class="eyebrow"><span>FIELD NOTES / EEG × E–I</span><span>{s['id']} / {len(slides):02}</span></div>
 <p class="question">學習問題 / {html.escape(s['question'])}</p><h1>{html.escape(s['title'])}</h1>
 <div class="content">{s['body']}</div><div class="bridge"><b>下一步 →</b> {html.escape(s['bridge'])}</div>
 <footer>來源 {links} · <a href="{wiki}" target="_blank" rel="noopener">Wiki 與證據</a><br>{html.escape(s['source_locator'])}</footer></section>''')
css=(R/'slides/theme.css').read_text();js=(R/'slides/interactions.js').read_text()
page='<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="dark"><title>從 EEG 到 E/I：互動教學</title><style>'+css+'</style></head><body><main>'+''.join(blocks)+'</main><nav aria-label="投影片導覽"><button id="prev" type="button">← 上一頁</button><span id="count" aria-live="polite"></span><progress id="progress" max="'+str(len(slides))+'" value="1" aria-label="簡報進度"></progress><button id="next" type="button">下一頁 →</button></nav><script>'+js+'</script></body></html>'
(R/'index.html').write_text(page)
print('Rendered',len(slides),'slides to index.html')
