import time
import tweepy
from textblob import TextBlob as Text

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGSE3AEAAAAAOUlLexwbCkajyAQiRi6OgOHVtFc%3D7RzzVJK73udoAU9H69SyUrtaUMJhbjyJQpA3XVHi3v7dQCN4V9'

client = tweepy.Client(bearer_token=bearer_token)

try:
    response = client.search_recent_tweets(query="Trump", max_results=10)
    if response.data:
        for tweet in response.data:
            print(tweet.text)
            analysis = Text(tweet.text)
            print(analysis.sentiment)
            if analysis.sentiment.polarity > 0:
                print('Positive')
            elif analysis.sentiment.polarity == 0:
                print('Neutral')
            else:
                print('Negative')
            print()
    else:
        print("No tweets found.")

except tweepy.TooManyRequests:
    print("Rate limit hit. Please wait a few minutes and try again.(Reset in 15 minutes)")
