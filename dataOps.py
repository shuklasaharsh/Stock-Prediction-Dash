import yfinance as yf
from datetime import date
import streamlit as st

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")


@st.cache
def loadData(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data
