import streamlit as st
import darts
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
Sale_to_List_table = pd.read_csv("Sales_to_List.csv")
Covid_Rate = pd.read_csv("https://raw.githubusercontent.com/biobotanalytics/covid19-wastewater-data/master/cases_by_county.csv")
Sandy = Covid_Rate.loc[Covid_Rate["name"] == 'San Diego County, CA']
below_list = pd.read_csv("Metro_pct_sold_below_list_uc_sfrcondo_sm_week.csv")
tblow_list = below_list.drop(columns = ["RegionID","SizeRank","RegionType","StateName"]).T
sandy_temp = tblow_list[17].to_frame()
Below_List_Price = sandy_temp.drop(["RegionName"])
dates = pd.to_datetime(Below_List_Price.index)
list_below_ratio = Below_List_Price[17].values
skice = {"Dates" : dates, "Percentage sold Under List Price" :list_below_ratio}
B_low_list = pd.DataFrame(data=skice)
above_list = pd.read_csv("Metro_pct_sold_above_list_uc_sfrcondo_week.csv")
tabov_list = above_list.drop(columns = ["RegionID","SizeRank","RegionType","StateName"]).T
sandy_temp_abov = tabov_list[17].to_frame()
Abov_List_Price = sandy_temp_abov.drop(["RegionName"])
dates_above = pd.to_datetime(Abov_List_Price.index)
list_above_ratio = Abov_List_Price[17].values
bove = {"Dates" : dates_above, "Percentage sold above list price" :list_above_ratio}
Percent_above_list_price = pd.DataFrame(data=bove)
# Median Sale Price: The median price at which homes across various geographies were sold.
Median_Sale_List = pd.read_csv("Metro_median_sale_to_list_uc_sfrcondo_sm_week.csv")
Median_list = Median_Sale_List.drop(columns = ["RegionID","SizeRank","RegionType","StateName"]).T
sandy_median = Median_list[17].to_frame()
Median_List_Price = sandy_median.drop(["RegionName"])
dates_median = pd.to_datetime(Median_List_Price.index)
medin_prices = Median_List_Price[17].values
medi = {"Dates" : dates_median, "Median sale to list Ratio" :medin_prices}
Median_sale_to_list_price = pd.DataFrame(data=medi)
# Days to Close (mean/median): Number of days between the listing going pending and the sale date.
Median_Close = pd.read_csv("Metro_median_days_to_close_uc_sfrcondo_sm_week.csv")
Median_clos = Median_Close.drop(columns = ["RegionID","SizeRank","RegionType","StateName"]).T
sandy_median_close = Median_clos[17].to_frame()
Median_Close_Price = sandy_median_close.drop(["RegionName"])
dates_median_close = pd.to_datetime(Median_Close_Price.index)
clos_prices = Median_Close_Price[17].values
med_clos = {"Dates" : dates_median_close, "Median days to close" :clos_prices}
Median_closing_days = pd.DataFrame(data=med_clos)
# Sale-to-List Ratio (mean/median): Ratio of sale vs. final list price.
# Price home actually sold for (sale) versus prices that home was listed online for (list)
Mean_Sale_List = pd.read_csv("Metro_mean_sale_to_list_uc_sfrcondo_sm_week.csv")
Mean_sales = Mean_Sale_List.drop(columns = ["RegionID","SizeRank","RegionType","StateName"]).T
mean_sales = Mean_sales[17].to_frame()
Mean_sales_Price = mean_sales.drop(["RegionName"])
dates_mean_sales = pd.to_datetime(Mean_sales_Price.index)
mean_prices = Mean_sales_Price[17].values
mean_sal = {"Dates" : dates_mean_sales, "Mean Sales to List Ratio" :mean_prices}
Mean_Selling_price = pd.DataFrame(data=mean_sal)
# Days to Close (mean/median): Number of days between the listing going pending and the sale date.
Mean_Close = pd.read_csv("Metro_mean_days_to_close_uc_sfrcondo_sm_week.csv")
mean_close_close = Mean_Close.drop(columns = ["RegionID","SizeRank","RegionType","StateName"]).T
mean_close_close = mean_close_close[17].to_frame()
mean_close_close_Price = mean_close_close.drop(["RegionName"])
dates_mean_close_close = pd.to_datetime(mean_close_close_Price.index)
mean_close_prices = mean_close_close_Price[17].values
mean_close_sal = {"Dates" : dates_mean_close_close, "Mean Days to Close" :mean_close_prices}
mean_close__days = pd.DataFrame(data=mean_close_sal)
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
st.title("Covid Cases in San Diego 2020 to present")
st.image("San_Diego_Covid_Cases.png")
st.title("San Diego Unemployment")
st.line_chart(SD_employ_fixing.set_index("Date"))
st.title("Covariate Forecast of Home Values using Covid Cases")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Coefficient of variation" , "3.42")
col2.metric("Mean Absolute Percentage Error (MAPE)" , "2.47")
col3.metric("Mean Absolute Ranged Relative Error (MARRE)" , "9.51")
col4.metric("Overall Perccentage error (OPE)" , "2.095")
st.image("Covariate Forecast of Home Values using Covid Cases.png")
#st.metric()
st.title("Univariate forecast of Home Prices using Oversampling")
st.image("Home Value Index OverSampling Forecast.png")
#st.metric()
st.title("Univariate forecast of Home Prices using Undersampling")
st.image("Home Value Index UnderSampling Forecast.png")
st.title("Covariate Forecast using Unemployment Data")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Coefficient of variation" , "7.92")
col2.metric("Mean Absolute Percentage Error (MAPE)" , "4.05")
col3.metric("Mean Absolute Ranged Relative Error (MARRE)" , "9.68")
col4.metric("Overall Perccentage error (OPE)" , "2.94")
st.image("Home Value Index Prophet Forecast using San Diego Unemployment as a covariate.png")
st.line_chart(Mean_Selling_price.set_index("Dates"))
#st.line_chart(Median_sale_to_list_price.set_index("Dates"))
st.title("Ratio of Homes Sold above List Price")
st.line_chart(Percent_above_list_price.set_index("Dates"))
st.image("Univariate Prediction of Homes Sold Above List Price using OverSampling.png")
st.title("Ratio of Homes Sold under List Price")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Coefficient of variation" , "22.84")
col2.metric("Mean Absolute Percentage Error (MAPE)" , "37.68")
col3.metric("Mean Absolute Ranged Relative Error (MARRE)" , "22.66")
col4.metric("Overall Perccentage error (OPE)" , "26.54")
st.line_chart(B_low_list.set_index("Dates"))
st.image("Univariate Prediction of Homes Sold Below List Price using OverSampling.png")
