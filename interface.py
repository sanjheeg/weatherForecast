import streamlit as sl
import pandas as pd
import plotly.express as px
from backend import get_data

sl.title("Weather Forecast")
place = sl.text_input("Place: ")
days = sl.slider("Forecast Days", min_value=1, max_value=5,help="select the number of forecasted days")
option = sl.selectbox("Data to view", ("Temperature", "Sky"))
sl.subheader(f"{option} for the next {days} days in {place}")

dates, temp = get_data(place, days, option)

figure = px.line(x=dates, y=temp, labels={"x": "Date", "y": "Temperature (C)"})
sl.plotly_chart(figure)