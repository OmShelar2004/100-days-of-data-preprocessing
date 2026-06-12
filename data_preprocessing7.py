import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("messy_employee.csv")
print(df)

# explore the data
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())


# check for missing values
print(df.isnull().sum())


#how many males and females are there in the dataset

print(df["Gender"].value_counts())

#how many departments are there in the dataset

print(df["Department"].value_counts())

#Standardize the department column by replacing the incorrect values with the correct values


df["Department"] = df["Department"].replace({
    "AI": "Artificial Intelligence",
    "A.I.": "Artificial Intelligence",
    "ML": "Machine Learning",
    "DS": "Data Science"})

#rStandardize the gender column by replacing the incorrect values with the correct values

df["Gender"] = df["Gender"].replace({
    "M": "Male",
    "male":"Male",
    "MALE":"Male",
    "F":"Female",
    "female":"Female",
    "FEMALE":"Female"})


print(df["Department"].unique())
print(df["Gender"].unique())

print(df)

