import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("employee_features.csv")
print(df)


#create new categories

df["Age_Groups"] = pd.cut(
    df["Age"],
    bins = [0,25,40,100],
    labels = ["young",  "mid", "senior"]
)

df["Salary_cat"] = pd.cut(
    df["Salary"],
    bins = [0,40000,70000,100000],
    labels = ["low","mid","high"]
)

print(df[["Age","Age_Groups"]].value_counts())
print(df[["Salary","Salary_cat"]].value_counts())

print(df["Salary_cat"].isnull().sum())
print(df["Age_Groups"].isnull().sum())
