import pandas as pd
import matplotlib.pyplot as plt

# reading the dataset
df = pd.read_csv('/Users/krish/Desktop/College Stuff/SMA/SMA-Pracs-main/Hashtag Analysis/ghana_nigeria_takedown_tweets.csv')

# Grouping the data and counting frequency of each hashtag
grouped = df.groupby('tweet_client_name')['hashtags'].apply(lambda x: pd.Series([tag for tags in x.dropna() for tag in tags.split()]).value_counts())

client_name = 'Twitter for Android'
fig,ax = plt.subplots(figsize = (10,15)) 
top_hashtags = grouped[client_name][1:6] # slicing 1st column to (6-1) i.e 5th column
ax.bar(top_hashtags.index, top_hashtags.values)
ax.set_title(f'Top 5 hashtags for {client_name}')
ax.set_xlabel('Hashtags')
ax.set_ylabel('Frequency')

plt.tight_layout()
plt.show()
