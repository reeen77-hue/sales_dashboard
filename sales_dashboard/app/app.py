from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# ==========
# データ読み込み
# ==========
project_root = Path(__file__).resolve().parents[1]
csv_path = project_root / "data" / "sales_daily.csv"

df = pd.read_csv(csv_path)
df["date"] = pd.to_datetime(df["date"])

st.title("📊 Sales Dashboard")
st.caption("Dummy sales data dashboard (store × product × gender × day)")

# ==========
# Sidebar フィルタ
# ==========
st.sidebar.header("Filters")

stores = sorted(df["store_id"].unique())
store = st.sidebar.selectbox("Store", stores)

genders = sorted(df["gender"].unique())
gender = st.sidebar.multiselect("Gender", genders, default=genders)

min_date = df["date"].min().date()
max_date = df["date"].max().date()
date_range = st.sidebar.date_input("Date range", value=(min_date, max_date))

start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])

# ==========
# データ絞り込み
# ==========
f = df[
    (df["store_id"] == store)
    & (df["gender"].isin(gender))
    & (df["date"] >= start_date)
    & (df["date"] <= end_date)
].copy()

# ==========
# KPI（transactions 本物版）
# ==========
total_amount = f["sales_amount"].sum()
total_qty = f["sales_qty"].sum()
total_txns = f["transactions"].sum()

asp = total_amount / total_qty if total_qty > 0 else 0
aov = total_amount / total_txns if total_txns > 0 else 0
upt = total_qty / total_txns if total_txns > 0 else 0

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Sales Amount", f"{total_amount:,.0f}")
c2.metric("Sales Qty", f"{total_qty:,.0f}")
c3.metric("Transactions", f"{total_txns:,.0f}")
c4.metric("AOV (Amount/Txn)", f"{aov:,.0f}")
c5.metric("UPT (Qty/Txn)", f"{upt:,.2f}")

st.divider()

# ==========
# Tabs
# ==========
tab_overview, tab_product, tab_gender = st.tabs(["Overview", "Product", "Gender"])

with tab_overview:
    st.subheader("Daily Sales Amount")
    daily = f.groupby("date", as_index=False)["sales_amount"].sum()
    fig = plt.figure()
    plt.plot(daily["date"], daily["sales_amount"])
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Sales Amount")
    st.pyplot(fig)

with tab_product:
    st.subheader("Top Products by Sales Amount")
    top = (
        f.groupby("product_code", as_index=False)["sales_amount"].sum()
        .sort_values("sales_amount", ascending=False)
        .head(10)
    )
    fig2 = plt.figure()
    plt.bar(top["product_code"].astype(str), top["sales_amount"])
    plt.xlabel("product_code")
    plt.ylabel("sales_amount")
    st.pyplot(fig2)
    st.dataframe(top.reset_index(drop=True))

with tab_gender:
    st.subheader("Sales Amount by Gender")
    g = f.groupby("gender", as_index=False)["sales_amount"].sum()
    g["share"] = (g["sales_amount"] / g["sales_amount"].sum()).fillna(0)
    fig3 = plt.figure()
    plt.bar(g["gender"], g["sales_amount"])
    plt.xlabel("gender")
    plt.ylabel("sales_amount")
    st.pyplot(fig3)

    g_show = g.copy()
    g_show["share"] = (g_show["share"] * 100).round(1).astype(str) + "%"
    st.dataframe(g_show.reset_index(drop=True))

st.divider()

# ==========
# Raw data
# ==========
with st.expander("Show raw data"):
    st.dataframe(f.sort_values("date").reset_index(drop=True))
