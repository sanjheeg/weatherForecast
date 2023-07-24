import streamlit as sl
import pandas as pd

sl.title("Weather Forecast")
place = sl.text_input("Place: ")
days = sl.slider("Forecast Days", min_value=1, max_value=5,help="select the number of forecasted days")
option = sl.selectbox("Data to view", ("Temperature", "Sky"))
sl.subheader(f"{option} for the next {days} days in {place}")