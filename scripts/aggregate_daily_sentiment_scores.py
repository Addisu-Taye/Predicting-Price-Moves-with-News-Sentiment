import pandas as pd
from textblob import TextBlob
import os

# === 1. Load Cleaned Analyst Ratings ===
cleaned_data_path = './data/cleaned_data/cleaned_analyst_ratings.csv'

if not os.path.exists(cleaned_data_path):
    raise FileNotFoundError(f"File not found: {cleaned_data_path}")

df = pd.read_csv(cleaned_data_path)

# === 2. Ensure 'headline' column exists ===
if 'headline' not in df.columns:
    raise ValueError("'headline' column is missing in the dataset.")

# === 3. Apply Sentiment Analysis ===
def analyze_sentiment(text):
    if isinstance(text, str) and text.strip():
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

df[['polarity', 'sentiment']] = df['headline'].apply(analyze_sentiment)

# === 4. Save updated cleaned data ===
df.to_csv(cleaned_data_path, index=False)
print(f"Sentiment columns added to: {cleaned_data_path}")

# === 5. Compute Average Daily Sentiment Scores ===
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['polarity', 'date'])

df_daily_sentiment = (
    df.groupby([df['stock'], df['date'].dt.date])['polarity']
    .mean()
    .reset_index()
)

df_daily_sentiment.columns = ['Stock', 'Date', 'Avg_Sentiment']

# === 6. Save Daily Sentiment Scores ===
output_path = './data/cleaned_data/aggregate_daily_sentiment_scores.csv'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df_daily_sentiment.to_csv(output_path, index=False)

print(f"Saved average daily sentiment scores to: {output_path}")
print(df_daily_sentiment.head())
