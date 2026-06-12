import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# Load the dataset

df = pd.read_csv("messy_data.csv")
print(df)

#explore the dataset

print(df.shape)
print(df.info())
print(df.describe())
print(df.columns)

#check for missing values
print(df.isnull().sum())

#checking min and max values for age and salary

print(df["Salary"].min())
print(df["Salary"].max())

print(df["Age"].min())
print(df["Age"].max())

#visualizing the outliers in age using boxplot

sns.boxplot(x=df["Age"])
plt.show()

#hanlding outliers 
df.loc[df["Age"]<0,"Age"] = pd.NA
df.loc[df["Age"]>100,"Age"] = pd.NA

print(df["Age"].isnull().sum()) 

#checking for duplicate values and dropping them

print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
print(df.shape)

print(df)


#handling missing values 

df["Age"].fillna(df["Age"].median(),inplace=True)
df["Salary"].fillna(df["Salary"].median(),inplace=True)
df["Department"].fillna(df["Department"].mode()[0],inplace=True)
df["Experience"].fillna(df["Experience"].median(),inplace=True)

print(df.isnull().sum())

#using Replace to convert ai into ARTIFICiAL INTELLIGENCE in the Department column

df["Department"]= df["Department"].replace("AI","ARTIFICIAL INTELLIGENCE")

print(df["Department"].unique())