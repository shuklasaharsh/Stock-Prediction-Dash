import streamlit as st  # Streamlit is used to get the frontend
from datetime import date  # DateTime for the time series analysis
import yfinance as yf  # YFinance gets Stock Data
import prophet
from plotly import graph_objects as go
import dataOps
import plotOps
import forecastOps

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.set_page_config(page_title="Stockd", page_icon="./data/favicon.ico", layout="centered")

body = '''
<style>
a {text-decoration: none;}
a.first  { left: 0%; position: relative; }
a.second { left: 45%; position: relative; }
a.third  { left: 85%; position: relative; }
.title {left:55%; position: relative;}
</style>

<div>
<a href="https://shuklasaharsh.herokuapp.com/" class="first">My Portfolio</a>
<a href="https://github.com/shuklasaharsh/" class="second">My Github</a>
<a href="https://amp.c4projects.tech" class="third">C4Projects</a>
</div>
<div class="title">
<h1>Stockd</h1>
</div>
'''

st.markdown(body, unsafe_allow_html=True)
stocks = ["AAPL", "GOOG", "MSFT", "GME", "^NSEI"]
selected_stock = st.selectbox("Select Stock", stocks)
n_years = st.slider("Years of prediction: ", 1, 4)
period = n_years * 365

data_load_state = st.text("Loading Data...")

data = dataOps.loadData(ticker=selected_stock)

data_load_state.text("Data Successfully Loaded")
st.subheader(f"Raw Data: {selected_stock}")
st.write(data.head())

plotOps.plotRawData(data)

forecast, future, model = forecastOps.trainModel(data, period)

st.subheader(f"Forecast: {selected_stock}")
st.write(forecast)
st.subheader(f"Forecast Chart: {selected_stock}")
forecastOps.plotForecast(model, forecast)
st.subheader(f"Individual Trends: {selected_stock}")
forecastOps.plotComponents(model, forecast)
