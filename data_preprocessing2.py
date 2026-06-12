import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["species"] = iris.target

print(df.head())

#preprocessing

print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())

#explore

print(df["species"].value_counts())

#average petal length per species

print(df.groupby("species")["petal length (cm)"].mean())

#identifying Correlation using  Heatmap

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(7,6))

sns.heatmap(df.corr(), annot=True)

plt.show()
            