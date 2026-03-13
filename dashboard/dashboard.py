import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

conn = sqlite3.connect("vitals.db")

st.title("AI Patient Monitoring Dashboard")

df = pd.read_sql("SELECT * FROM vitals", conn)

st.write(df)

if len(df) > 0:

    fig = px.line(df, y="heart_rate", title="Heart Rate")

    st.plotly_chart(fig)

    alerts = df[df["status"] == "ANOMALY"]

    st.write("⚠️ Anomaly Alerts")

    st.write(alerts)