# 工作紀錄

## 2026-11-23 — Phase 1

- 工作目錄起初為空且不是 Git repository。已根據使用者提供的九項確認事項整理需求；未虛構訪談逐字稿。
- 讀取課程 PDF 文字：課程要求先討論後建立 Wiki、至少 ingest 五篇、設計有檢查與回退的流程、反思。PDF 視作參考資料，不覆蓋使用者規格。
- `git init` 在沙箱內遭拒（`.git: Operation not permitted`）；已提出權限請求。來源與其狀態將逐篇記錄。

## 2026-11-23 — 來源草稿與第一次檢查

- 建立六篇 paper note 和九個概念頁，皆待審，尚無一篇完成全部 ingest 關卡。S01/S02/S04/S06 全文入口可讀；S03/S05 起初被瀏覽驗證頁阻擋，後經授權網路下載全文 HTML 至暫存目錄。未公開全文。
- `python3 scripts/graph.py` 實際執行：五項中三項通過、兩項失敗，依 N4 規則停止。見 `reports/run-1.txt`。
- 查詢測試發現短詞匹配與索引頁偏重，局部修改排序後重新執行五題；Graph 重測仍未達資料及 evidence map 門檻。見 `reports/final-report.md`。

## 2026-11-23 — 延續工作

- 六篇全文均取得，逐篇核對方法、結果、限制及引用；見 `reports/ingest-checks.md`。這是聚焦閱讀與人工對照，並非獨立科學審查。
- Graph 第三次執行：Wiki lint 五項通過，證據地圖／HTML 結構通過，見 `reports/run-3.txt`。
- Playwright 初次找不到其內建 Chromium，切換已安裝 Chrome；沙箱啟動失敗，經授權執行成功。指數圖自動縱軸縮放掩蓋斜率差異，改固定範圍並加入畫布變化檢查，重測通過。
