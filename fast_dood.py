
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
datam=pd.read_csv("C:\\Users\\buğra\\Desktop\\Top 50 Fast-Food Chains in USA.csv")
print(datam.columns)
print(datam.shape)
print(datam.info())
name=datam["Fast-Food Chains"]
stor=datam["Company Stores"]
franchised=datam["Franchised Stores"]
a=datam['U.S. Systemwide Sales (Millions - U.S Dollars)']
avarage=datam["Average Sales per Unit (Thousands - U.S Dollars)"]

plt.figure(figsize=(10,6))
a=datam.sort_values("Company Stores" , ascending=False)
sns.barplot(y="Company Stores"  , x="Fast-Food Chains",   data=a )
plt.xticks(rotation=90)
plt.xlabel("Company Name")
plt.title("Company Stores")
plt.grid(True)
plt.show()

b=datam.sort_values("Franchised Stores" , ascending=False)
sns.barplot(x="Fast-Food Chains" , y="Franchised Stores" , data=b)
plt.xticks(rotation=90)
plt.xlabel("Company Name")
plt.title("Franchised Stores")
plt.grid(True)
plt.show()

plt.plot("Fast-Food Chains","Franchised Stores" ,data=datam)
plt.plot("Fast-Food Chains","Company Stores" ,data=datam)
plt.xticks(rotation=90)
plt.title("karşılaştırma")
plt.show()