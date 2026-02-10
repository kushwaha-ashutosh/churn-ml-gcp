import streamlit as st
import pandas as pd

st.title("Customer Churn Dashboard")

df = pd.read_csv("data/sample_features.csv")

churn_rate = df["label_churned"].mean()

st.metric("Overall Churn Rate", f"{churn_rate:.2%}")

st.bar_chart(df["label_churned"].value_counts())
