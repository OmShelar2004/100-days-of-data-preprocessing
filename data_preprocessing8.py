import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("employee_chaos.csv")
print(df)

# explore the data

print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

# check for missing values
print(df.isnull().sum())

# values of the department column

print(df["Department"].unique())

# values of the gender column

print(df["Gender"].unique())
print(df["Gender"].nunique())


#min and max values of the salary column
print(df["Salary"].min())
print(df["Salary"].max())

#min and max values of the age column
print(df["Age"].min())
print(df["Age"].max())

#visualizing the outliers in the salary column using boxplot

sns.boxplot(x=df["Salary"])
plt.show()

#visualizing the outliers in the Age column using boxplot

sns.boxplot(x=df["Age"])
plt.show()

#filling missing age values with NA

df.loc[df["Age"]<0,"Age"] = pd.NA
df.loc[df["Age"]>100,"Age"] = pd.NA

print(df["Age"].isnull().sum())

# filling missing values of the department column with the mode
df["Department"].fillna(df["Department"].mode()[0], inplace=True)


#finding duplicate values and dropping them

print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
print(df.shape)

# standardize the department column by replacing the incorrect values with the correct values

df["Department"] = df["Department"].replace({
    "AI": "Artificial Intelligence",
    "A.I.": "Artificial Intelligence",
    "ML": "Machine Learning",
    "DS": "Data Science"
})


# standardizing the Gender column by replacing the incorrect values with the correct values

df["Gender"] = df["Gender"].replace({
    "M": "Male",
    "male" : "Male",
    "MALE" : "Male",
    "F": "Female",
    "female" :"Female",
    "FEMALE" : "Female",

})

print(df)

# cleaning Join date column


df["Join_Date"]=pd.to_datetime(df["Join_Date"],errors="coerce")#convert to datetime



df["Join_Date"] = df["Join_Date"].dt.strftime("%Y-%m-%d")



#filling missing dates

df["Join_Date"].fillna(df["Join_Date"].mode()[0],inplace= True)

print(df)