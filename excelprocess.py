import pandas as pd

data= pd.read_excel("Salesdata.xlsx")
print(data.head())
# print(data.head(2))
# print(data.describe())
print(data["Price"])
print(data["Name"])