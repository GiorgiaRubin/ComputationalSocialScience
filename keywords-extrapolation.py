import nltk
from nltk.corpus import stopwords
import collections
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.transforms import count_bboxes_overlapping_bbox

#Transorm the texts of tweets into a long list of words 
only_tweets = []
for tweet in user_tweet:
  only_tweets.append(tweet[1])

all_in_one = ''.join(only_tweets)

list_of_words = all_in_one.split()

#Delete unnecessary words for keyword selection (such as conjunctions, articles, etc.)
nltk.download('stopwords')
True

stop_words = set(stopwords.words('english'))

words_to_consider = []
for word in list_of_words:
  if word in stop_words:
     pass
  else:
    words_to_consider.append(word)

#Count how often the words considered were repeated in the different tweets
counts_words = collections.Counter(words_to_consider)
counts_words.most_common()

#Wordcloud visualization
unique_tweet = []
ut=''
for i in only_tweets:
  unique_tweet.append(str(i))
  text= ut.join(unique_tweet)

plt.figure(figsize=(10,10))
wordcloud=WordCloud().generate(text)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
