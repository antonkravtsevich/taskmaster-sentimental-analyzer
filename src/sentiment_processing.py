from textblob import TextBlob


class SentimentProcessor:

    def __init__(self):
        pass

    def get_polarity(self, text):
        analyzis = TextBlob(text)
        return analyzis.sentiment.polarity
