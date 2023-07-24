import streamlit as sl
import pandas as pd
import plotly.express as px
from backend import get_data

sl.title("Weather Forecast")
place = sl.text_input("Place: ")
days = sl.slider("Forecast Days", min_value=1, max_value=5,help="select the number of forecasted days")
option = sl.selectbox("Data to view", ("Temperature", "Sky"))

if len(place) == 0:
    place = "Tokyo"

sl.subheader(f"{option} for the next {days} days in {place}")

filtered = get_data(place, days, option)

if option == "Temperature":
    temp = [i["main"]["temp"] for i in filtered]
    print(filtered)
    dates = [i["dt_txt"] for i in filtered]
    figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
    sl.plotly_chart(figure)

if option == "Sky":
    filtered = [i["weather"][0]["main"] for i in filtered]



