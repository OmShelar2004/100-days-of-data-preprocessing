import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset

df = sns.load_dataset("titanic")
print(df.head())

#explore the dataset

print(df.shape)
print(df.columns)
print(df.info())
print(df.describe   ())

#check for missing values

print(df.isnull().sum())

#drop columns with too many missing values
df.drop(columns=["deck"],inplace=True)

#checking duplicate values

print(df.duplicated().sum())

#drop duplicate values

df_no_dup = df.drop_duplicates(inplace=True)
print(df.shape)


print(df["class"].value_counts())

#Which class had the highest survival rate?
print(df.groupby("class")["survived"].mean())

#which sex had the highest survival rate?
print(df.groupby("sex")["survived"].mean())


#sorting the dataset by sex,fare,survived and class
print(
    df.sort_values(by="fare", ascending=False)
      [["class","sex","fare","survived"]]
      .head(10)
)