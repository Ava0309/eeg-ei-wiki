# 執行與驗收報告

時間：2026-11-23（Asia/Taipei）。核心問題：EEG 頻譜特徵能否可靠地提供腦部興奮／抑制平衡資訊？

## 文獻與 Wiki

六篇全文已取得；對每篇的方法、結果、討論及下列引用位置進行聚焦閱讀和核對，完成初步整合。此處的 PASS 指本專案執行者完成以上步驟，不代表逐字覆核全文或通過獨立科學審查。

| ID | 來源 | 對照位置與貢獻 |
|---|---|---|
| S01 | Donoghue 2020 | Fig. 2、Methods、Extended Data：背景／候選峰模型及擬合限制 |
| S02 | Donoghue 2022 | Box 1、Fig. 1、3、Conclusion：頻帶功率與非週期背景的混淆 |
| S03 | Cochrane 2026 | Methods、Results、Discussion：睡眠人類同步 EEG/MRS；Glx/GABA+ 並非突觸電流比 |
| S04 | Gao 2017 | §2–4、Fig. 1：模型、大鼠 LFP、獼猴 ECoG，不能混同頭皮 EEG |
| S05 | Salvatore 2024 | EEG Analysis、Results、Discussion、Fig. 1、2、6：小鼠硬腦膜外皮質 EEG 的操弄結果及限制 |
| S06 | Sun & Mou 2023 | Introduction、§1.1.2、§3–4：EEG 處理、資料增強與跨受試者泛化 |

每篇紀錄及當時的 lint 結果見 [ingest-checks.md](ingest-checks.md)。[Wiki Index](../wiki/index.md) 串接 paper notes、九個概念頁與跨研究比較。逐頁稿與 evidence map 保存在 [evidence-map.json](../slides/evidence-map.json)，每筆包含學習目標、Wiki 路徑、原始來源、主張與定位；HTML 由同一檔生成。

## Graph 與真實測試

- 初期 `reports/run-1.txt` 與 `reports/run-2.txt` 保留了五篇 ingest 門檻及 evidence map 缺失的失敗，不覆寫歷史。
- 後續 `python3 scripts/graph.py --attempt 1` 實際執行 N4 與 N6/N9：Wiki lint 五項通過，12 頁 evidence map 和 HTML 結構檢查通過，見 `run-3.txt`。再次執行見 `run-4.txt`。失敗時腳本輸出回退節點與次數；人工執行局部修正，不聲稱自動修復。
- Playwright 搭配系統 Chrome 在 1440×900 與 390×844 檢查 12 頁頁碼、按鈕、方向鍵、兩個滑桿、橫向溢出、JavaScript runtime error；結果 errors 0、failures 0。截圖在本資料夾。這不代表所有螢幕尺寸都已覆蓋。
- 科學逐頁對照見 [content-review.md](content-review.md)，由製作者執行；**獨立科學審查尚未完成**。程式檢查無法證明每個科學結論。

## 問題、局部回退與反思

1. 初期 N1/N2 未完成五篇核對，N6 缺 evidence map；流程停下。後續逐篇處理，再建立地圖並重跑，結構關卡通過。
2. N10 初次測試找不到 Playwright 自帶瀏覽器，改用已安裝 Chrome；在沙箱啟動失敗，經授權在沙箱外成功。
3. N9/N10 實際檢視發現指數圖每次自動縮放縱軸，導致 β 變動被掩蓋。退回 N9 固定縱軸、增加畫布前後內容變化檢查；重新執行桌面與手機測試均通過。
4. 早期 N5 查詢曾因短詞匹配而出現無關結果，已限制完整詞匹配並降低索引頁權重；五題示範見 `query-examples.txt`。

目前記錄不足以統計哪個節點在長期運作中最常出錯；本次有可觀察的問題分布於 N1/N2、N5 與 N9/N10。改善方式是在單篇 ingest 時檢查定位詞，在生成 HTML 後立刻測試互動前後圖像；已落實後者，但仍須補上更嚴格的來源語意與獨立審查關卡。

## 發布與剩餘限制

Repository：[Ava0309/eeg-ei-wiki](https://github.com/Ava0309/eeg-ei-wiki)；[Wiki](https://github.com/Ava0309/eeg-ei-wiki/tree/main/wiki)；[GitHub Pages 教學簡報](https://ava0309.github.io/eeg-ei-wiki/)。GitHub Pages 初次建置狀態為 built，公開網址已以 Chrome 開啟並執行同一套互動與版面測試，errors 0、failures 0。未完成獨立科學審查；DOI 自動檢查是格式檢查，無法單獨證明書目正確。圖表是合成資料，不是實驗數據。
