import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# reading the dataset
df = pd.read_csv('/Users/krish/Desktop/College Stuff/SMA/SMA-Pracs-main/_animes.csv')

# Check Shape
print(df.shape) # (rows, columns)

# Check each data type of columns and missing values using info()
print(df.info())

# Summary Statistics
print('\n',df.describe())

# Checking percentage of missing values
print(df.isnull().sum() / df.shape[0] * 100)

df = df.drop(['uid'], axis=1)

# visualizing the data
anime_df = df.head(20)
sns.countplot(data = anime_df, x= 'episodes')
plt.show()

# plotting a scatter plot
plt.scatter(anime_df['score'], anime_df['popularity'])
plt.xlabel('Score')
plt.ylabel('Popularity')
plt.title('Score Vs Popularity')
plt.show()

# plotting a bar chart
plt.bar(anime_df['title'], anime_df['popularity'])
plt.xticks(rotation = 90)
plt.show()

# # distribution of valence per hit/flop
# target_dict = {"Flop": df.loc[df.target == 0, "valence"], 
#                "Hit": df.loc[df.target == 1, "valence"]}
# ax[1].boxplot(target_dict.values(), labels = target_dict.keys())
# ax[1].set_title("Distribution of Valence By 'Hit' vs. 'Flop'")
# ax[1].set_ylabel("Valence")

