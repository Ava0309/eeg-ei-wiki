# 作業繳交說明

- **主題與成果：** EEG 訊號、頻譜、興奮／抑制平衡與機器學習的繁體中文教學 Wiki；[Repository](https://github.com/Ava0309/eeg-ei-wiki)、[Wiki](../wiki/index.md)、[15 頁 HTML](../index.html) 與 [GitHub Pages](https://ava0309.github.io/eeg-ei-wiki/)。頁面互動使用 Synthetic Data。
- **科學審查：** [獨立 N8 報告](n8-independent-final.md) 對 15 頁重要主張為 **SCOPED PASS**；S05 指定原文方法、結果及圖已補查。此判斷不是六篇逐字全文審讀、原始研究資料重算或所有互動輸入的認證。Exponent 不是直接量得的突觸 E/I 比，MRS 代謝物比也不等同突觸電流比。
- **Graph／Loop：** [工作流程](../workflow/graph.md) 記錄人工節點、自動關卡、回退和最多三次失敗的停止條件。runner 不會自動修復或自動完成獨立審查；N5 完整覆蓋率仍須人工評估。
- **實際測試與歷史：** [執行報告](final-report.md) 保留舊版與新版的真實失敗、修正和測試；[最新整合狀態](workflow-runs/20261123T150115Z-47042dda/state.json) 的 lint、evidence map／HTML、數學、N9 圖表和 N10 本機桌機／手機測試通過。首次沙箱啟動 Chrome 失敗與沙箱外重跑均已保存。此測試不等於公開網站本輪重新部署或重新驗證。
