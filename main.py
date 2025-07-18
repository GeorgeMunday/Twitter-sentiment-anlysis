import tweepy
from textblob import TextBlob as Text

bearer_token = 'YOUR_BEARER_TOKEN'

client = tweepy.Client(bearer_token=bearer_token)

try:
    response = client.search_recent_tweets(query="Trump", max_results=10)

    if response.data:
        for tweet in response.data:
            print(tweet.text)
            analysis = Text(tweet.text)

            polarity = analysis.sentiment.polarity
            subjectivity = analysis.sentiment.subjectivity

            print(f"Polarity: {polarity}")
            print(f"Subjectivity: {subjectivity}")

            # Polarity sentiment label
            if polarity > 0:
                print('Sentiment: Positive')
            elif polarity == 0:
                print('Sentiment: Neutral')
            else:
                print('Sentiment: Negative')

            # Subjectivity label (optional, for fun)
            if subjectivity > 0.5:
                print('Tone: Subjective')
            elif subjectivity < 0.5:
                print('Tone: Objective')
            else:
                print('Tone: Balanced')

            print()

    else:
        print("No tweets found.")

except tweepy.TooManyRequests:
    print("Rate limit hit. Please wait a few minutes and try again.Request limits resets every 15 minutes(response code: 429)")

