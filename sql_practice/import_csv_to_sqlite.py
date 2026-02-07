from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(r"C:\Users\PC_User\Desktop\sales_dashboard")
CSV_PATH = ROOT / "data" / "sales_daily.csv"
DB_PATH = ROOT / "sql_practice" / "sales.db"

df = pd.read_csv(CSV_PATH)

# 念のため：列名チェック
expected = ["date","store_id","product_code","gender","sales_qty","sales_amount","transactions"]
missing = [c for c in expected if c not in df.columns]
if missing:
    raise ValueError(f"CSVに必要な列がありません: {missing}\n実際の列: {list(df.columns)}")

with sqlite3.connect(DB_PATH) as con:
    df.to_sql("sales", con, if_exists="replace", index=False)

print("OK: imported", len(df), "rows into", DB_PATH)
print("columns:", list(df.columns))
print(df.head(3))
