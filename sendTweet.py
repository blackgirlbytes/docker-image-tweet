# send Tweet to Twitter with tweepy

import tweepy
import os

# Consumer keys and access tokens, use for tweepy.Client authentication which are stored in Codespaces secrets
client = tweepy.Client(
    consumer_key=os.environ['CONSUMER_KEY'],
    consumer_secret=os.environ['CONSUMER_SECRET_KEY'],
    access_token=os.environ['ACCESS_TOKEN'],
    access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
)

# create variable called tweet with the text that says "I wrote this tweet with Copilot!"
tweet = "I sent this tweet with Copilot!"

# Send Tweet with client.create_tweet with text as argument
response = client.create_tweet(text=tweet)

# Print response
print(response)


