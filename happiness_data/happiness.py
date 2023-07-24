import streamlit as sl
import pandas as pd
import plotly.express as px

df = pd.read_csv("happy.csv")
# col = df.columns
col = ["gdp", "happiness", "generosity"]

sl.header("In search for happiness")
x = sl.selectbox("x-axis", col)
y = sl.selectbox("y-axis", col)

x_plot = df[x]
y_plot = df[y]

sl.subheader(f"{x} and {y}")
figure = px.scatter(x=x_plot, y=y_plot, labels={"x": x, "y": y})
sl.plotly_chart(figure)
