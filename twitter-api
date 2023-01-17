import os
import tweepy as tw
import pandas as pd
import re

#Define the keys
consumer_key = 'enteryourpersonalkey'
consumer_secret_key= 'enteryourpersonalkey'
access_token_key= 'enteryourpersonalkey'
access_token_secret_key='enteryourpersonalkey'

auth = tw.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token_key, access_token_secret_key)

api = tw.API(auth, wait_on_rate_limit=True)

#Define the search term and the date_since date as variables
search_words = "#nft"
date_since = "2022-09-10"  

#Remove Retweets
new_search = search_words + " -filter:retweets"

#Collect tweets
tweets = tw.Cursor(api.search,
                       q=new_search,
                       lang="en", 
                       since=date_since).items(3000)

#Remove URL and emoji from the text
def remove_url(txt):
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

#Return the name of the user and its own tweet without signs and in lower case                   
user_tweet = [[tweet.user.screen_name, remove_url(tweet.text.lower())] for tweet in tweets]
user_tweet
