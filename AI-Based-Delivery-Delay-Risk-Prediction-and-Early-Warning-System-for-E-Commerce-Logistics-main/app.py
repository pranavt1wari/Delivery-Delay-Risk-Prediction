import streamlit as st
import pandas as pd

st.set_page_config(page_title="Delivery Delay Risk Prediction")

st.title("AI-Based Delivery Delay Risk Prediction")

st.subheader("dataset preview")

df = pd.read_csv("data/processed/processed_delivery_data.csv")
st.dataframe(df.head())


