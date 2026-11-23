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

## 舊版 12 頁：Graph 與真實測試紀錄

- 初期 `reports/run-1.txt` 與 `reports/run-2.txt` 保留了五篇 ingest 門檻及 evidence map 缺失的失敗，不覆寫歷史。以下 12 頁測試和來源核對均屬舊版，不代表已測試正式的 15 頁版。
- 後續 `python3 scripts/graph.py --attempt 1` 實際執行 N4 與 N6/N9：Wiki lint 五項通過，12 頁 evidence map 和 HTML 結構檢查通過，見 `run-3.txt`。再次執行見 `run-4.txt`。失敗時腳本輸出回退節點與次數；人工執行局部修正，不聲稱自動修復。
- Playwright 搭配系統 Chrome 在 1440×900 與 390×844 檢查 12 頁頁碼、按鈕、方向鍵、兩個滑桿、橫向溢出、JavaScript runtime error；結果 errors 0、failures 0。截圖在本資料夾。這不代表所有螢幕尺寸都已覆蓋。
- 科學逐頁對照見 [content-review.md](content-review.md) 與 [本次十二頁來源重新核對](source-recheck-20261123.md)，均由製作者執行；**獨立科學審查尚未完成**。程式檢查無法證明每個科學結論。

## 舊版 12 頁：問題、局部回退與反思

1. 初期 N1/N2 未完成五篇核對，N6 缺 evidence map；流程停下。後續逐篇處理，再建立地圖並重跑，結構關卡通過。
2. N10 初次測試找不到 Playwright 自帶瀏覽器，改用已安裝 Chrome；在沙箱啟動失敗，經授權在沙箱外成功。
3. N9/N10 實際檢視發現指數圖每次自動縮放縱軸，導致 β 變動被掩蓋。退回 N9 固定縱軸、增加畫布前後內容變化檢查；重新執行桌面與手機測試均通過。
4. 早期 N5 查詢曾因短詞匹配而出現無關結果，已限制完整詞匹配並降低索引頁權重；五題示範見 `query-examples.txt`。

依既有紀錄的定性比較，**N10 Browser QA 是本次最常暴露問題的節點**：它暴露了瀏覽器啟動／環境問題，也暴露圖表尺度造成視覺結果不正確；這不是長期頻率統計，也不將同一問題的多次重跑計為多個錯誤。瀏覽器啟動屬測試環境問題；圖表的自動縮放則在 N9 產生、由 N10 發現。

原本在 N10 才檢查互動；舊版修正時新增 `tests/render_plot.cjs`，在 N9 渲染後先比較 β=0.2 與 2.4 時固定畫布座標的曲線位置。舊版真實結果見 [render-plot.txt](qa-20261123/render-plot.txt)：起點約 36.5 與 37.5，末端約 46 與 151.5，PASS；之後舊版桌機與手機 N10 重跑結果見 [browser.txt](qa-20261123/browser.txt)，errors 0、failures 0。N9 檢查是單獨執行，並未宣稱已由 `graph.py` 自動調度。另在舊版 12 頁來源重新核對第 3 頁時，發現 S04 的 ECoG 章節位置誤寫為 §2.5，已依原文修正為 §2.7。

## 發布與剩餘限制

Repository：[Ava0309/eeg-ei-wiki](https://github.com/Ava0309/eeg-ei-wiki)；[Wiki](https://github.com/Ava0309/eeg-ei-wiki/tree/main/wiki)；[GitHub Pages 教學簡報](https://ava0309.github.io/eeg-ei-wiki/)。公開網址在舊版與新版發布時均曾以 Chrome 開啟測試；版本對應與保存紀錄見各節。未完成 N8 獨立科學審查；DOI 自動檢查是格式檢查，無法單獨證明書目正確。圖表是合成資料，不是實驗數據。

## 正式版 15 頁：2026-11-23 教學品質改版與測試

原本 12 頁以短句與卡片為主；新版先補足 [Wiki 教學基礎](../wiki/concepts/teaching-foundations.md)，再產生 15 頁學習問題、圖解、例子、銜接及來源。DFT 位於新版第 5 頁，Machine Learning 位於新版第 14 頁。新互動涵蓋取樣混疊、雙正弦與 DFT、Welch 平均、背景／候選峰與頻帶功率、參數化四步、固定座標 exponent，以及小測驗；所有曲線皆明示 Synthetic Data。

[新版 15 頁 Teaching Quality Review](teaching-redesign-20261123/teaching-quality-review.md) 是製作者教學自審，與前述舊版 12 頁來源核對不同，兩者都不是獨立科學審查。首次 N9 畫布測試因新版座標而失敗，已保留原始輸出並修正測試；後續數學、Wiki lint、15 頁 evidence／HTML、桌機與手機瀏覽器測試的實際輸出在 [teaching-redesign-20261123](teaching-redesign-20261123/)。數學測試檢查 DFT 振幅、混疊、七個 Welch 窗、PSD 積分及尺度、合成背景對 band power 的影響。瀏覽器檢查不取代真實初學者使用測試。獨立科學審查 N8 仍未完成。
