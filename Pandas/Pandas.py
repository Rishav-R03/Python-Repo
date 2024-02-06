import pandas as pd
# 2 main data types 
series = pd.Series(["BMW","Toyota","Honda"])
series

# serise = 1-dimensional 
colours = pd.Series(["Red","Blue","White"])
colours

# DataFrames = 2-dimensional
car_data = pd.DataFrame({"Cars":series,"Colour":colours})
car_data

#Import data 
car_sales = pd.read_csv("/content/sample_data/Car_sales.csv")
car_sales

# Exporting data frame
car_sales.to_csv("exported-car-sales.csv")
# it is exported to the default directory
#use index = False to remove the previous data file's serial number column

#attribute
car_sales.dtypes
car_sales.columns
# Function
# car_sales.to_csv()

car_columns = car_sales.columns
car_sales.index 

car_sales.describe() #