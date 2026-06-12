import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
df = sns.load_dataset("tips")
print(df.head())

#inspecting the dataset
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())

#explore
print(df["sex"].value_counts())
print(df["day"].value_counts())
print(df["smoker"].value_counts())

#average total bill per day
print(df.groupby("day")["total_bill"].mean())

#which gender gives hugher tips on average
print(df.groupby("sex")["tip"].mean())

#do smokers or non smokers give higher tips on average
print(df.groupby("smoker")["tip"].mean())




#Visua;ization

sns.boxplot(x=df["tip"])
plt.show()

#average tip on different days

print(df.groupby("day")["tip"].mean())

#sorting tip

print(df.sort_values(by="tip",ascending=False).head())