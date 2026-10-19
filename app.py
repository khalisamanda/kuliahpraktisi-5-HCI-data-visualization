from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Online Shopper Insights", layout="wide")
st.title("Dashboard Perilaku Belanja Online")
st.caption("Sumber: UCI Online Shoppers Purchasing Intention Dataset")
path=Path("online_shoppers_clean.csv")
if not path.exists():
    st.warning("Letakkan online_shoppers_clean.csv hasil notebook di folder yang sama dengan app.py.")
    st.stop()
df=pd.read_csv(path)
if "Revenue" in df.columns: df["Revenue"]=df["Revenue"].astype(str).str.lower().map({"true":True,"false":False}).fillna(False)
if "Month" in df.columns:
    months=sorted(df["Month"].dropna().unique().tolist())
    selected=st.multiselect("Filter bulan",months,default=months)
    df=df[df["Month"].isin(selected)]
col1,col2,col3=st.columns(3)
col1.metric("Jumlah sesi",f"{len(df):,}")
col2.metric("Sesi dengan pembelian",f"{int(df['Revenue'].sum()):,}")
col3.metric("Conversion rate",f"{df['Revenue'].mean():.2%}" if len(df) else "0%")
if "VisitorType" in df.columns:
    summary=df.groupby("VisitorType",as_index=False).agg(Sesi=("Revenue","size"),Conversion=("Revenue","mean"))
    st.plotly_chart(px.bar(summary,x="VisitorType",y="Sesi",title="Jumlah sesi per tipe pengunjung"),use_container_width=True)
    st.plotly_chart(px.bar(summary,x="VisitorType",y="Conversion",title="Conversion rate per tipe pengunjung",labels={"Conversion":"Conversion rate"}),use_container_width=True)
with st.expander("Lihat data yang digunakan"):
    st.dataframe(df.head(500),use_container_width=True)
st.caption("Interpretasi: hubungan antarfitur bersifat deskriptif dan tidak membuktikan sebab-akibat.")
