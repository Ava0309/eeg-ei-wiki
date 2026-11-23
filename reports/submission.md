# 作業繳交說明

1. **LLM Wiki 主題與介紹：** From EEG Signals to Excitation–Inhibition Balance，串連 EEG、頻譜參數化、E/I 研究與機器學習，提供初學者繁體中文概念、公式及研究限制。六篇來源已進行方法、結果及引用位置的聚焦閱讀與核對。
2. **Repository 與 Wiki：** [GitHub Repository](https://github.com/Ava0309/eeg-ei-wiki)；[Wiki 首頁](https://github.com/Ava0309/eeg-ei-wiki/blob/main/wiki/index.md)。
3. **教學 HTML：** [GitHub Pages 簡報](https://ava0309.github.io/eeg-ei-wiki/)，共 15 頁，含標示 Synthetic Data 的取樣、FFT、Welch、頻譜分解、參數化步驟及 exponent 互動；另有逐頁問題、公式拆解、三篇研究的條件比較與小測驗。
4. **Graph／Loop：** 逐篇 ingest → 引用核對 → Wiki 整合與 lint → Wiki 檢索 → 證據卡與大綱 → 逐頁稿 → 獨立審查 → HTML → 瀏覽器 QA。詳細 Mermaid 與回退路線見 [Graph](https://github.com/Ava0309/eeg-ei-wiki/blob/main/workflow/graph.md)。腳本會執行 N4 與 N6/N9 結構關卡並顯示失敗回退；局部修正由人執行，最多三輪。實際 HTML 已先產生，獨立審查尚未完成，流程因此仍未閉合。
5. **真實檢查與修正：** 最初缺少五篇 ingest 與 evidence map，兩項失敗紀錄保留；後續 lint、15 頁 evidence map 與 HTML 結構檢查通過。舊版瀏覽器實測曾發現圖表自動縮放掩蓋 β 變化，退回 N9 固定縱軸並重測；舊版來源核對也把 S04 ECoG 定位由 §2.5 修正為 §2.7。正式 15 頁版的 DFT 教學位於第 5 頁，假想 Machine Learning 例子位於第 14 頁。新版圖表數學、桌機及手機互動測試結果見[執行報告](https://github.com/Ava0309/eeg-ei-wiki/blob/main/reports/final-report.md)。
6. **反思與審查：** 依既有紀錄定性判斷，N10 Browser QA 最常暴露問題：瀏覽器執行環境與 N9 所產生的圖表尺度問題都在此浮現；這不是長期次數統計。圖表檢查已前移至 N9，在渲染後比較不同 β 下固定畫布座標的曲線位置，再進行 N10 測試。製作者執行的[舊版 12 頁來源核對](https://github.com/Ava0309/eeg-ei-wiki/blob/main/reports/source-recheck-20261123.md)與[新版 15 頁 Teaching Quality Review](https://github.com/Ava0309/eeg-ei-wiki/blob/main/reports/teaching-redesign-20261123/teaching-quality-review.md)是不同紀錄，兩者都不是獨立科學審查。**N8 獨立科學審查仍未完成**；exponent 不可當成直接測得的 E/I 比。

本次 15 頁原文逐項重新核對及局部修正詳見 [N8 審查紀錄](https://github.com/Ava0309/eeg-ei-wiki/blob/main/reports/n8-independent-review.md)。核對者曾參與製作，**N8 仍為 PENDING**；修正後 Wiki／證據結構、圖表數學及桌機／手機測試通過，不代表已完成獨立科學審查。
