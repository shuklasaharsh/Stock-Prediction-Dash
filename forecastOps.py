from prophet import Prophet
from plotly import graph_objects as go
import streamlit as st
from prophet.plot import plot_plotly


def refactorData(data):
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
    return df_train


def trainModel(data, period):
    data = refactorData(data)
    model = Prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=period)
    forecast = model.predict(future)
    return forecast, future, model


def plotRawData(forecast):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['trend'], name='median trend'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['trend_lower'], name='lower trend'))
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['trend_upper'], name='upper trend'))
    fig.layout.update(title_text="Forecast", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


def plotForecast(model, forecast):
    fig = plot_plotly(model, forecast)
    st.plotly_chart(fig)


def plotComponents(model, forecast):
    fig = model.plot_components(forecast)
    st.write(fig)

