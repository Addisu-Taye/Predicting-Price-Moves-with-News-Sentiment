import pandas as pd

def analyze_sentiment_price_correlation(price_csv, sentiment_csv):
    # Load data
    df_price = pd.read_csv(price_csv)
    df_sentiment = pd.read_csv(sentiment_csv)

    # Convert date columns
    df_price['Date'] = pd.to_datetime(df_price['Date'])
    df_sentiment['date'] = pd.to_datetime(df_sentiment['date'])

    # Aggregate sentiment by date
    df_sentiment_grouped = df_sentiment.groupby(df_sentiment['date'].dt.date).agg({'polarity': 'mean'}).reset_index()
    df_sentiment_grouped['date'] = pd.to_datetime(df_sentiment_grouped['date'])

    # Merge on date
    df_merged = pd.merge(df_price, df_sentiment_grouped, left_on='Date', right_on='date', how='inner')

    if len(df_merged) > 10:
        correlation = df_merged['Close'].corr(df_merged['polarity'])
        return correlation, df_merged[['Date', 'Close', 'polarity']]
    else:
        return None, df_merged[['Date', 'Close', 'polarity']]

# Example usage:
# correlation, merged_data = analyze_sentiment_price_correlation('AAPL_historical.csv', 'AAPL_sentiment.csv')
# if correlation is not None:
#     print("Correlation:", correlation)
# else:
#     print("Not enough overlapping data to calculate correlation.")
