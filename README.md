# 📊 Sales Dashboard（分析ダッシュボード）

## 概要 / 目的

本プロジェクトは、**小売店舗（アパレル）を想定した売上データを可視化する分析ダッシュボード**です。
Pythonでダミーデータを設計・生成し、Streamlitを用いて

* 売上の全体像
* 商品・性別などの切り口
* KPI（売上・数量・客数・客単価など）
  を**直感的に把握できるUI**として実装しています。

「機械学習以前に、まず“正しく数字を見て説明できるか”」を重視した構成です。

---

## 使用技術

* Python
* pandas
* numpy
* matplotlib
* Streamlit

---

## データ設計（ダミーCSV）

`sales_daily.csv`（Pythonスクリプトで自動生成）

| 列名           | 内容                             |
| ------------ | ------------------------------ |
| date         | 日付                             |
| store_id     | 店舗ID                           |
| product_code | 商品コード（例：501 / 502 / 505 / 511） |
| gender       | 性別（Men / Women）                |
| sales_qty    | 販売数量                           |
| sales_amount | 売上金額                           |
| transactions | 取引数（客数の近似）                     |

※ transactions は「1人で複数点購入する」ケースを想定し、数量より小さくなるよう設計しています。
---

## データ / 分析フロー概要（Pipeline）

```text
Raw CSV (sales_daily.csv)
        │
        ▼
Data Filtering (store / gender / date)
        │
        ▼
KPI Calculation
(Sales, Qty, Transactions, AOV, UPT)
        │
        ▼
Visualization (Streamlit)
 - Line chart (daily sales)
 - Bar chart (product / gender)
 - Raw data table


## ダッシュボードでできること

### 🎛 フィルタ（サイドバー）

* 店舗選択
* 性別選択（複数可）
* 期間指定

→ フィルタ操作に応じて、すべてのKPI・グラフがリアルタイムに更新されます。

---

### 📌 KPI表示（上部）

* **Sales Amount**：売上金額合計
* **Sales Qty**：販売数量合計
* **Transactions**：取引数（客数）
* **AOV（Amount / Transaction）**：客単価
* **UPT（Qty / Transaction）**：1取引あたり点数

売上だけでなく、「客数」「客単価」「点数」まで分解して把握できる構成です。

---

### 📂 タブ構成

#### Overview

* 日別売上推移（折れ線グラフ）
* 期間内の売上トレンドを把握

#### Product

* 商品別売上（Top N）
* 売上構成・主力品番の把握

#### Gender

* 性別別売上
* 売上構成比（％）を表示

---

### 🔍 Raw Data 表示

* フィルタ後の生データを折りたたみ表示
* 数値の根拠を確認可能

---

## 工夫ポイント

* **UIと分析ロジックを分離**し、読みやすさ・拡張性を意識
* ダミーデータでも、実務を想定した列設計（transactions など）
* フィルタ → KPI → 詳細分析、の自然な分析フロー

---

## 今後の改善案（実務を想定した拡張）

本ダッシュボードは「現場での数字把握」を目的とした最小構成です。
実務利用を想定した場合、以下の拡張が考えられます。

* セール期間フラグ追加（通常期 vs セール期の比較）
* 在庫データ追加（欠品による機会損失の可視化）
* 商品 × 性別のクロス分析
* 実データ接続やクラウド公開（共有・運用）


---

## 起動方法

```bash
python -m streamlit run app/app.py
```
---

## プロジェクト構成

```text
sales_dashboard/
├─ data/
│  └─ sales_daily.csv
├─ app/
│  └─ app.py
├─ src/
│  └─ data_loader.py（必要に応じて分離）
└─ README.md

---

## 補足

本プロジェクトは、**データ分析・可視化の基礎設計力を示すポートフォリオ**として作成しています。


