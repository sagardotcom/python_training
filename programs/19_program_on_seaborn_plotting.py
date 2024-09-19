"""
Seaborn: Plotting graph
"""
print("iris flower data:")
print("-"*20)
# ------------

import pandas as pd

iris_data_df = pd.read_csv("Iris.csv")
print(iris_data_df.head(5))

print("#"*40, end="\n\n")
#################################

print("plotting violinplot")
print("-"*20)
# ------------

import seaborn as sns
import matplotlib.pyplot as plt

sns.violinplot(data=iris_data_df)
plt.show()

print("#"*40, end="\n\n")
#################################

print("plotting violinplot")
print("-"*20)
# ------------

import seaborn as sns
import matplotlib.pyplot as plt

sns.violinplot(data=iris_data_df, x='Species', y='SepalLengthCm')
plt.show()

print("#"*40, end="\n\n")
#################################

print("plotting lineplot")
print("-"*20)
# ------------

import seaborn as sns
import matplotlib.pyplot as plt

sns.lineplot(data=iris_data_df, x='Species', y='SepalLengthCm')
plt.show()

print("#"*40, end="\n\n")
#################################


print("plotting relplot")
print("-"*20)
# ------------

import seaborn as sns
import matplotlib.pyplot as plt

sns.relplot(data=iris_data_df, x='Species', y='SepalLengthCm')
plt.show()

print("#"*40, end="\n\n")
#################################

print("plotting scatterplot")
print("-"*20)
# ------------

import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(data=iris_data_df, x='PetalLengthCm', y='SepalLengthCm')
plt.show()

print("#"*40, end="\n\n")
#################################