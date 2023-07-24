import streamlit as sl
import pandas as pd
import plotly.express as px


def get_data(days):
    dates = ["2022", "2023"]
    temp = [10, 11]
    temp = [days * i for i in temp]
    return dates, temp


sl.title("Weather Forecast")
place = sl.text_input("Place: ")
days = sl.slider("Forecast Days", min_value=1, max_value=5,help="select the number of forecasted days")
option = sl.selectbox("Data to view", ("Temperature", "Sky"))
sl.subheader(f"{option} for the next {days} days in {place}")

dates, temp = get_data(days)

figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
sl.plotly_chart(figure)