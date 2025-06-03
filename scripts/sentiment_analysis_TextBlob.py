import pandas as pd
from textblob import TextBlob

# Load cleaned data
cleaned_data_path = './data/cleaned_data/cleaned_analyst_ratings.csv'
df = pd.read_csv(cleaned_data_path)

# Ensure 'headline' column exists
if 'headline' not in df.columns:
    raise ValueError("❌ 'headline' column is missing in the dataset.")

# Define sentiment analysis function
def analyze_sentiment(text):
    if isinstance(text, str) and text.strip():  # Ensure text is not NaN or empty
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiment = 'positive'
        elif polarity < 0:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        return pd.Series([polarity, sentiment])
    else:
        return pd.Series([None, 'neutral'])

# Apply sentiment analysis
df[['polarity', 'sentiment']] = df['headline'].apply(analyze_sentiment)

# Save updated cleaned data (overwrite existing)
df.to_csv(cleaned_data_path, index=False)
print(f"✅ Sentiment columns added and saved in the cleaned file: {cleaned_data_path}")

# Preview result
print(df[['headline', 'polarity', 'sentiment']].head())
