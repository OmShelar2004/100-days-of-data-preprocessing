import pandas as pd

df = pd.read_csv("titanic.csv")


# data exploration
print(df.head())
print(df.shape)
print(df.info())            
print(df.describe())
print(df.isnull().sum())

# data cleaning
df.drop(columns=["Cabin"],inplace = True)
print(df.columns)

df["Age"].fillna(df["Age"].median(), inplace=True)

df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

print(df.isnull().sum())


# data encoding

df["Sex"] = df["Sex"].map({
    "male" : 0,
    "female" : 1
    })

print(df["Sex"])

#one hot encoding
df = pd.get_dummies(df,columns=["Embarked"])

print(df.head())

# Drop useless columns

df.drop(columns=["Name","Ticket","PassengerId"],inplace = True)

print(df.columns)
print(df.info())
print(df.shape)

#visualiize outliers
import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(x=df["Age"])
plt.show()

print(df["Age"].mean())#Find Average Age

print(df["Age"].max())#Find Max Age

print(df["Age"].min())#Find Min Age

print(df["Sex"].value_counts())#Find Count

print(df["Survived"].value_counts())


#groupby
print(df.groupby("Sex")["Survived"].mean())

#visualize survival rate by

sns.countplot(x="Survived",data=df)
plt.show()
print(df.head())