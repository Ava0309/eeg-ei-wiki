# 作業繳交說明

1. **LLM Wiki 主題與介紹：** From EEG Signals to Excitation–Inhibition Balance，串連 EEG、頻譜參數化、E/I 研究與機器學習，提供初學者繁體中文概念、公式及研究限制。六篇來源已進行方法、結果及引用位置的聚焦閱讀與核對。
2. **Repository 與 Wiki：** [GitHub Repository](https://github.com/Ava0309/eeg-ei-wiki)；[Wiki 首頁](https://github.com/Ava0309/eeg-ei-wiki/blob/main/wiki/index.md)。
3. **教學 HTML：** [GitHub Pages 簡報](https://ava0309.github.io/eeg-ei-wiki/)，共 12 頁，含標示 Synthetic Data 的 EEG 波形／頻譜與 exponent 互動。
4. **Graph／Loop：** 逐篇 ingest → 引用核對 → Wiki 整合與 lint → Wiki 檢索 → 證據卡與大綱 → 逐頁稿 → 獨立審查 → HTML → 瀏覽器 QA。詳細 Mermaid 與回退路線見 [Graph](https://github.com/Ava0309/eeg-ei-wiki/blob/main/workflow/graph.md)。腳本會執行 N4 與 N6/N9 結構關卡並顯示失敗回退；局部修正由人執行，最多三輪。實際 HTML 已先產生，獨立審查尚未完成，流程因此仍未閉合。
5. **真實檢查與修正：** 最初缺少五篇 ingest 與 evidence map，兩項失敗紀錄保留；後續 lint、12 頁 evidence map 與 HTML 結構檢查通過。瀏覽器實測曾發現圖表自動縮放掩蓋 β 變化，退回 N9 固定縱軸並重測。此次另補第 4 頁 DFT 符號與第 11 頁假想 ML 例子，並在來源核對時把 S04 ECoG 定位由 §2.5 修正為 §2.7。最新 N9 圖表、桌機及手機互動測試結果見[執行報告](https://github.com/Ava0309/eeg-ei-wiki/blob/main/reports/final-report.md)。
6. **反思：** 依現有紀錄定性判斷，N10 Browser QA 最常暴露問題：瀏覽器執行環境與 N9 所產生的圖表尺度問題都在此浮現；這不是虛構的長期次數統計。圖表檢查現已前移至 N9：在渲染後比較不同 β 下固定畫布座標的曲線位置，再進行完整 N10 測試。科學內容的十二頁重新對照由製作者執行，**獨立科學審查仍待完成**；exponent 不可當成直接測得的 E/I 比。
