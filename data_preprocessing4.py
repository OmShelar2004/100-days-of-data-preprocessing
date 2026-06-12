import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = sns.load_dataset("penguins")
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.columns)

# Explore the dataset
print(df["species"].value_counts())
print(df["island"].value_counts())
print(df["sex"].value_counts())

# Average bill length by species
print(df.groupby("species")["bill_length_mm"].mean())

# Average bill depth by species
print(df.groupby("species")["bill_depth_mm"].mean())

# Average flipper length by species
print(df.groupby("species")["flipper_length_mm"].mean())

# Average body mass by species
print(df.groupby("species")["body_mass_g"].mean())

#sorting body mass
print(df.sort_values(by ="body_mass_g",ascending=False).head(10))

#avrerage body maas of male and female
print(df.groupby("sex")["body_mass_g"].mean())



#VISUALIZATION

# Boxplot of body mass by species
sns.boxplot(x=df["body_mass_g"])
plt.show()


#filling missing values with mode
df["sex"].fillna(df["sex"].mode()[0], inplace=True)
print(df.isnull().sum())