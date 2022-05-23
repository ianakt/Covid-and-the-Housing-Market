# Final_project_Covid19




Our journey so far....

link to slides: https://docs.google.com/presentation/d/1fWEJO-d1I_VNijgDdGBT22hTEK-FKRyce9HMPWvdutk/edit?usp=sharing

What is our project about?

How covid effected the home buying experience in San Diego between 2020 and 2022?

Why did we do this?

The Covid Pandemic is a major event that will define us for the rest of our lives. This is the time of our lives where we are transitioning to full adulthood, finally getting all of the worries, rewards, and responsobilities of this stage of development. A defining step of adulthood is owning your own home, which appears to be more difficult this time than in ages past. We would like to know if the housing market will follow the trends of covid cases, or follow historical trends of the housing market in the future. We will look at how Covid Cases affected various elements of the housing market such as Sale to List Price, Housing Price, and Rent Price. Additionally we will see if employment affects the housing market.


Datasets:

Biobot analytics RNA concentration in Waste water
Biobot analytics cases per 100,000

Data exploration:

The Prophet Model:

In this model, Unemployment is used as a covariate to predict the value of the housing market over time. The processing of this data is shown below

      # Added "Dates" Column that shows the month and year of each value e.g. 2020-01 
      SD_employ_fixing.insert(0, "Dates", pd.to_datetime(SD_employ_fixing["Date"]).dt.to_period('M'), True)
      # Drop date column, this date column came with the data
      SD_employ_fixing = SD_employ_fixing.drop(columns = "Date")
      # rename new "Dates" column to "Date"
      SD_employ_fixing = SD_employ_fixing.rename(columns = {"Dates" : "Date"})
      
      # Merged Home_values and SD_employ to 1 tablw
      SD_em_HV = SD_employ_fixing.merge(Home_values, how = "inner", on = "Date")
      # changed "Date" column to time stamp in preparation for the ML Model
      SD_em_HV = SD_em_HV.set_index("Date").to_timestamp()

      # Made a dataframe for each column of "SD_em_HV"
      SD_Unemployment_to_series = pd.DataFrame(SD_em_HV["Unemployment Rate"])
      SD_Value_to_series = pd.DataFrame(SD_em_HV["Home Value Index"])


      # Changed to a time series
      SD_Unemployment_series = TimeSeries.from_dataframe(SD_Unemployment_to_series)
      SD_Value_series = TimeSeries.from_dataframe(SD_Value_to_series)

The training data was split by year, the training data set is pre 2016, and the values to predict are post 2016, also covariates were used as a supplement to the training dataset as future covariates. Within the darts library, future covariates are values that cover the same time span as dataset used as train test. 

![image](https://user-images.githubusercontent.com/68198233/169725363-38a97fda-7ee6-4512-bebb-efa53e971059.png)



![Home Value Index Prophet Forecast using San Diego Unemployment as a covariate](https://user-images.githubusercontent.com/68198233/169723874-42ef036d-65a3-4509-a416-abebfc00039e.png)





ML Model

This is still under construction. For now our plan is to have univariate analysis on a few key features of the housing market, and covid cases. We will have a multivariate model, and see if it is better than the univariate. Our measure of understading if covid effected the housing market significantly is to see whether the univariate, or the multivariate model performs better. 1 indicator is shown below

![image](https://user-images.githubusercontent.com/68198233/168510099-dc1340c3-1c6a-4b2c-bfad-0854c74b45d4.png)


Under Sampling







Dashboard

![image](https://user-images.githubusercontent.com/68198233/168511680-6d9ec811-8297-4089-b3c5-a6e6bae94e28.png)


Abhitesh:

COVID Deaths by Sex & Age

https://data.cdc.gov/NCHS/Provisional-COVID-19-Deaths-by-Sex-and-Age/9bhg-hcku


This is my final project.

Home Values for San Diego


<img width="1129" alt="Screen Shot 2022-05-15 at 2 43 53 PM" src="https://user-images.githubusercontent.com/95302013/168488888-ca882961-5d9f-4470-8b0c-ecbc23a9cc3c.png">

