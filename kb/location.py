import pandas as pd
import matplotlib.pyplot as plt

# reading and printing the dataset
df = pd.read_csv('/Users/krish/Desktop/College Stuff/SMA/SMA-Pracs-main/Location Analysis/sample.csv')

# dropping the rows that have NaN Values
df = df.dropna()
# print(df['Tweet Location'].head()) # prints only 1 column

# Adding the locations to a list
location_list = []
for location in df['Tweet Location']:
    location_list.append(location)

# Creating a frequency distribution of the location data
location_frequency = pd.Series(location_list).value_counts()

# Visualizing the frequency distribution using bar chart
location_frequency.head(25).plot(kind = 'bar')

plt.title('Top 25 Most Common Locations')
plt.xlabel('Location')
plt.ylabel('Frequency')
plt.show()
