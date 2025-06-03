import pandas as pd
import matplotlib.pyplot as plt

# Load data
df_price = pd.read_csv("TSLA_historical_data.csv")
df_sentiment = pd.read_csv("TSLA_data.csv")

# Parse dates
df_price['Date'] = pd.to_datetime(df_price['Date'])
df_sentiment['date'] = pd.to_datetime(df_sentiment['date'])

# Filter sentiment for the target date
focus_date = pd.to_datetime("2019-12-11")
sentiment_on_date = df_sentiment[df_sentiment['date'].dt.date == focus_date.date()]['polarity'].mean()

# Filter price data +/- 5 days
price_window = df_price[(df_price['Date'] >= focus_date - pd.Timedelta(days=5)) &
                        (df_price['Date'] <= focus_date + pd.Timedelta(days=5))]

# Plot
fig, ax1 = plt.subplots(figsize=(10, 5))

# Plot closing prices
ax1.plot(price_window['Date'], price_window['Close'], color='blue', marker='o', label='Closing Price')
ax1.axvline(x=focus_date, color='red', linestyle='--', label='Sentiment Date')
ax1.set_xlabel("Date")
ax1.set_ylabel("Closing Price (USD)", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Add sentiment on a second y-axis
ax2 = ax1.twinx()
ax2.set_ylabel("Sentiment Polarity", color='green')
ax2.plot([focus_date], [sentiment_on_date], marker='o', color='green', label='Sentiment Polarity')
ax2.tick_params(axis='y', labelcolor='green')

# Titles and legend
plt.title("Tesla (TSLA) Closing Price and Sentiment Around 2019-12-11")
fig.tight_layout()
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))
plt.grid(True)
plt.show()
