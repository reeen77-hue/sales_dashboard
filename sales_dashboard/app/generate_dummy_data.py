from pathlib import Path
import numpy as np
import pandas as pd

# ==========
# 設定
# ==========
SEED = 42
START_DATE = "2026-01-01"
N_DAYS = 60
STORES = ["store_001", "store_002"]
PRODUCTS = [501, 502, 505, 511]
GENDERS = ["Men", "Women"]

np.random.seed(SEED)

# ==========
# パス設定
# ==========
project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"
data_dir.mkdir(exist_ok=True)

# ==========
# データ生成
# ==========
dates = pd.date_range(START_DATE, periods=N_DAYS)

rows = []
for date in dates:
    for store in STORES:
        for product in PRODUCTS:
            for gender in GENDERS:
                qty = np.random.poisson(lam=8)
                price = np.random.randint(8000, 15000)

                # 取引数（客数の近似）
                txns = max(1, int(np.round(qty / np.random.uniform(1.5, 3.0))))

                rows.append(
                    {
                        "date": date,
                        "store_id": store,
                        "product_code": product,
                        "gender": gender,
                        "sales_qty": qty,
                        "sales_amount": qty * price,
                        "transactions": txns,
                    }
                )

df = pd.DataFrame(rows)

# ==========
# CSV出力
# ==========
csv_path = data_dir / "sales_daily.csv"
df.to_csv(csv_path, index=False, encoding="utf-8-sig")

print(f"CSV generated: {csv_path}")
