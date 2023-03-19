from nltk.tokenize import WordPunctTokenizer, WhitespaceTokenizer
from nltk.corpus import stopwords
from nltk.stem import *
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import csv

tweets = []
unchanged_tweets = []
with open("tweets.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        tweets.append(row)
        unchanged_tweets.append(row)


# Step 1:
#   Remove Duplicate Spaces between tweet's words
for i, tweet in enumerate(tweets):
    new_tweet = re.sub(r'\s+', ' ', str(tweet))
    tweets[i] = new_tweet

# Step 2:
#   Make text's words Lower case
for i, tweet in enumerate(tweets):
    new_tweet = tweet.lower()
    tweets[i] = new_tweet

# Step 3:
#   Remove Handles ( Usernames ) from Tweets
for i, tweet in enumerate(tweets):
    new_tweet = re.sub('@[\w]+', '', str(tweet))
    tweets[i] = new_tweet

# Step 4:
#   Remove punctuation, special characters and numbers from tweets
for i, tweet in enumerate(tweets):
    new_tweet = re.sub("[^a-z#&%\$ ]+", '', str(tweet))
    tweets[i] = new_tweet


# Step 5:
#   Apply Tokenization
for i, tweet in enumerate(tweets):
    new_tweet = WhitespaceTokenizer().tokenize(tweet)
    tweets[i] = new_tweet


# Step 6:
#   Removing Stop words
stop_words = set(stopwords.words('english'))
for i, tweet in enumerate(tweets):
    new_tweet = [w for w in tweet if not w in stop_words]
    tweets[i] = new_tweet

# Step 7:
#   Remove Words with len less than 3
for i, tweet in enumerate(tweets):
    new_tweet = [w for w in tweet if len(w) > 2]
    tweets[i] = new_tweet

# Step 8:
#   Stemming
porter = PorterStemmer()
for i, tweet in enumerate(tweets):
    new_tweet = [porter.stem(w) for w in tweet]
    tweets[i] = new_tweet

# rebuild tweets
rebuild_tweets = [None]*len(tweets)
for i, tweet in enumerate(tweets):
    new_tweet = ' '.join(tweet)
    rebuild_tweets[i] = new_tweet

# all words of tweets and their freq
all_words = [word for tweet in tweets for word in tweet]
c = Counter(all_words)
print("Top 5 Words:")
print(c.most_common(5))

# Word Cloud
wordcloud = WordCloud(width = 600, height = 600, background_color ='white', min_font_size = 12).generate(" ".join(all_words))

plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

string_of_All = " ".join(all_words)
trend_reg = re.compile(r"#\w+")
trends = Counter(trend_reg.findall(string_of_All))
trends = trends.most_common(5)
print(trends)
plt.bar([title for title, freq in trends], [freq for title, freq in trends])
plt.title("Trending Hashtags")
plt.xticks(rotation=90)
plt.show()

header = ['original tweet', 'preprocessed tweet']


with open('tweets_processed.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    all = []
    for i in range(len(unchanged_tweets)):
        all.append([unchanged_tweets[i], rebuild_tweets[i]])

    writer.writerows(all)




#print(tweets[20])
