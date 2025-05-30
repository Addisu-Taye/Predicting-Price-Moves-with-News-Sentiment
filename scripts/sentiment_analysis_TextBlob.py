import pandas as pd
from textblob import TextBlob

# Load CSV file
df = pd.read_csv('.//data//cleaned_data//cleaned_data.csv')

# Function to compute sentiment polarity and label
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    return pd.Series([polarity, sentiment])

# Apply the sentiment analysis
df[['polarity', 'sentiment']] = df['headline'].apply(analyze_sentiment)

# Save the results or display
print(df[['headline', 'polarity', 'sentiment']].head())
df.to_csv('sentiment_output.csv', index=False)
