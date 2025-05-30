import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Setup ---
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('pastel')
output_folder = 'eda_plot'
os.makedirs(output_folder, exist_ok=True)

# --- Load and Clean Data ---
df = pd.read_csv('sentiment_output_ALL.csv', parse_dates=['date'])
df.dropna(subset=['stock', 'polarity', 'sentiment', 'publisher', 'date', 'headline'], inplace=True)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date'])

# --- Feature Engineering ---
df['headline_len'] = df['headline'].str.len()
df['word_count'] = df['headline'].str.split().apply(len)
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.to_period('M')

# --- Subplot 1: Text Feature Distributions ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(df['headline_len'], bins=40, ax=axes[0])
axes[0].set_title('Headline Length Distribution')
axes[0].set_xlabel('Characters')

sns.histplot(df['word_count'], bins=30, ax=axes[1])
axes[1].set_title('Headline Word Count Distribution')
axes[1].set_xlabel('Words')

plt.tight_layout()
plt.savefig(f'{output_folder}/01_text_feature_distributions.png')
plt.close()

# --- Subplot 2: Time Series Analysis ---
fig, axes = plt.subplots(2, 1, figsize=(12, 8))

# Articles per Year
yearly_counts = df.groupby('year').size()
yearly_counts.plot(ax=axes[0])
axes[0].set_title('Articles Per Year')
axes[0].set_ylabel('Count')
axes[0].set_xlabel('Year')

# Sentiment by Year
sentiment_year = df.groupby(['year', 'sentiment']).size().unstack()
sentiment_year.plot(ax=axes[1])
axes[1].set_title('Sentiment Distribution by Year')
axes[1].set_ylabel('Count')
axes[1].set_xlabel('Year')

plt.tight_layout()
plt.savefig(f'{output_folder}/02_time_series_analysis.png')
plt.close()

# --- Subplot 3: Sentiment and Polarity ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Sentiment Pie Chart
df['sentiment'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=axes[0])
axes[0].set_ylabel('')
axes[0].set_title('Sentiment Distribution')

# Polarity Histogram
sns.histplot(df['polarity'], bins=40, kde=True, ax=axes[1])
axes[1].set_title('Polarity Score Distribution')

plt.tight_layout()
plt.savefig(f'{output_folder}/03_sentiment_polarity.png')
plt.close()

# --- Subplot 4: Top Entities ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Top Stocks
top_stocks = df['stock'].value_counts().nlargest(10)
sns.barplot(y=top_stocks.index, x=top_stocks.values, ax=axes[0])
axes[0].set_title('Top 10 Stocks')
axes[0].set_xlabel('Mentions')

# Top Publishers
top_publishers = df['publisher'].value_counts().nlargest(10)
sns.barplot(y=top_publishers.index, x=top_publishers.values, ax=axes[1])
axes[1].set_title('Top 10 Publishers')
axes[1].set_xlabel('Mentions')

plt.tight_layout()
plt.savefig(f'{output_folder}/04_top_entities.png')
plt.close()

# --- Subplot 5: Sentiment by Selected Stocks ---
tickers_of_interest = ['AAPL', 'GOOGL', 'TSLA', 'AMZN','META','MSFT','NVDA']
filtered_df = df[df['stock'].isin(tickers_of_interest)]

plt.figure(figsize=(12, 6))
sns.countplot(data=filtered_df, x='stock', hue='sentiment')
plt.title('Sentiment Distribution per Selected Stock')
plt.tight_layout()
plt.savefig(f'{output_folder}/05_sentiment_selected_stocks.png')
plt.close()

# --- Export Summary Stats ---
text_stats = df[['headline_len', 'word_count']].describe().transpose()
yearly_summary = df.groupby('year').size().reset_index(name='article_count')

text_stats.to_csv(f'{output_folder}/text_summary.csv')
yearly_summary.to_csv(f'{output_folder}/yearly_article_count.csv')

print("✅ EDA completed with grouped subplots. Plots and tables saved to 'eda_plot'")
