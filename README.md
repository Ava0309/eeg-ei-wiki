# From EEG Signals to Excitation–Inhibition Balance

繁體中文 EEG → 頻譜 → 興奮／抑制平衡 → 機器學習教學專案。15 頁互動式教學簡報由六篇來源支撐；六篇全文的主要方法、結果與限制已做聚焦閱讀和引用核對；15 頁重要主張已完成限定範圍的獨立科學審查；不代表六篇逐字審讀。核心問題：EEG 頻譜特徵能否可靠提供 E/I 平衡資訊？

- [開啟線上教學簡報](https://ava0309.github.io/eeg-ei-wiki/)（[本機 HTML](index.html) 可直接開啟）；[Wiki 首頁](wiki/index.md)；[跨研究比較](wiki/comparisons/evidence.md)。
- [需求](docs/requirements.md)；[來源與狀態](raw/sources.json)；[逐頁證據與逐頁稿](slides/evidence-map.json)；[Graph](workflow/graph.md)；[執行報告](reports/final-report.md)。
- 查詢實際 Wiki：`python3 scripts/query.py "What is an aperiodic exponent?"`。這是關鍵詞檢索，非語意生成。
- 自動關卡與半自動回退：`python3 scripts/graph.py`；需 Node、Playwright 與 Chrome，依環境設定 `NODE_PATH`。失敗後人工修復並以 `--resume <state.json>` 繼續，記錄與範圍見 [Graph](workflow/graph.md)；不自動修文，也不以程式取代科學審查。
- 重新產生 HTML：`python3 scripts/render.py`。投影片文字與來源從 `slides/evidence-map.json` 讀取，互動與樣式分別由 `slides/interactions.js`、`slides/theme.css` 提供；數值測試執行 `node tests/teaching_math.cjs`。
- 瀏覽器測試：安裝 Playwright 並確保 `tests/browser.cjs` 的 Chrome 路徑適用後，執行 `node tests/browser.cjs`；測試桌機與手機、鍵盤、滑桿、橫向溢出與 runtime error。
- 頻譜與波形皆為 Synthetic Data。指數是模型參數，非直接量測突觸 E/I；MRS Glx/GABA+ 也不等同突觸電流比。
