import streamlit as st
import pandas as pd
import numpy as np
import torch
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime
st.title("Home Values in San Diego 2020 to 2022")
Home_values = pd.read_excel("San_Diego_Home_Value_Index.xlsx")
HV = Home_values.set_index("Date")
SanDiego_Employment = pd.read_csv("SDUT.csv", parse_dates=True, infer_datetime_format=True)
SD_employ_fixing = pd.DataFrame(
    {"Date": pd.to_datetime(SanDiego_Employment["MONTH_DATES"]),
     "Unemployment Rate" : SanDiego_Employment["unemployment rate"] })
#      # Added "Dates" Column that shows the month and year of each value e.g. 2020-01 
# SD_employ_fixing.insert(0, "Dates", pd.to_datetime(SD_employ_fixing["Date"]).dt.to_period('M'), True)
# # Drop date column, this date column came with the data
# SD_employ_fixing = SD_employ_fixing.drop(columns = "Date")
# # rename new "Dates" column to "Date"
# SD_employ_fixing = SD_employ_fixing.rename(columns = {"Dates" : "Date"})
# # Merged Home_values and SD_employ to 1 tablw
# SD_em_HV = SD_employ_fixing.merge(Home_values, how = "inner", on = "Date")
# # changed "Date" column to time stamp in preparation for the ML Model
# SD_em_HV = SD_em_HV.set_index("Date").to_timestamp()
# # Made a dataframe for each column of "SD_em_HV"
# SD_Unemployment_to_series = pd.DataFrame(SD_em_HV["Unemployment Rate"])
# SD_Value_to_series = pd.DataFrame(SD_em_HV["Home Value Index"])
st.line_chart(HV)
st.title("San Diego Unemployment")
st.line_chart(SD_employ_fixing.set_index("Date"))
st.title("Home Value Index UnderSampling Forecast")
st.image('./Home Value Index UnderSampling Forecast.png')
st.title("Home Value Index OverSampling Forecast")
st.image('Home Value Index OverSampling Forecast.png')
st.title("Home Value Index Prophet Forecast using Unemployment")
st.image('Home Value Index Prophet Forecast using San Diego Unemployment as a covariate.png')
