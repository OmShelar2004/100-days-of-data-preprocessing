import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("employee_messy_case_study.csv")
print(df)

#explore the data

print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())



#detecting the outliers

print(df["Age"].min())
print(df["Age"].max())

print(df["Salary"].min())
print(df["Salary"].max())


#visualizing the outliers using boxplot

sns.boxplot(x=df["Age"])
plt.show()

sns.boxplot(x=df["Salary"])
plt.show()


#finding duplicates

print(df.duplicated().sum())

#exploring unique values of columns

print(df["Age"].unique())
print(df["Department"].unique())
print(df["Gender"].unique())

#dropping employee Id

df = df.drop_duplicates(subset=[
    "Name",
    "Age",
    "Gender",
    "Department",
    "Salary",
    "Experience",
    "Join_Date"
])

#dropping duplicates

df.drop_duplicates(inplace = True)

print(df.duplicated().sum())




#replacing outliers with na

df.loc[df["Age"]>100,"Age"] = pd.NA
df.loc[df["Age"]<0,"Age"] = pd.NA

df.loc[df["Salary"]>100000,"Salary"] = pd.NA
df.loc[df["Join_Date"]=="banana","Join_Date"] = pd.NA

print(df["Age"])
print(df["Name"])
print(df["Salary"])
print(df["Join_Date"])
print(df.columns)

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


print(df["Gender"].unique())
print(df["Department"].unique())

#encoding the gender using map function

df["Gender_to_code"]= df["Gender"].map({
    "Male" : 0,
    "Female" :1,
})

print(df["Gender_to_code"])

print(df)

#filling missing values

df["Age"] = df["Age"].fillna(df["Age"].median())

df["Salary"] = df["Salary"].fillna(df["Salary"].median())

df["Department"] = df["Department"].fillna(
    df["Department"].mode()[0]
)

df["Experience"] = df["Experience"].fillna(
    df["Experience"].median()
)

#standardising the Join_date column's value

df["Join_Date"] = pd.to_datetime(
    df["Join_Date"],
    errors="coerce",
    dayfirst=True
)

print(df["Join_Date"].dtype)

#creating features

df["Age_groups"] = pd.cut(
    df["Age"],
    bins=[0,25,40,100],
    labels = ["young","mid","senior"]
                          )

df["Exp_groups"] = pd.cut(
    df["Experience"],
    bins = [0,2,5,10],
    labels = ["junior","mid","senior"]
)
