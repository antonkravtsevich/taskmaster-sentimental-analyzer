from textblob import TextBlob

# using simple textblob analyz to return sentiment info
def get_polarity(text):
    analyzis = TextBlob(text)
    return analyzis.sentiment.polarity