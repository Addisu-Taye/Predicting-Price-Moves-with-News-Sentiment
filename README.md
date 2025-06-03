# Predicting Price Moves with News Sentiment
This project explores how financial news sentiment and technical indicators can be used to analyze and predict short-term stock price movements.

The analysis is based on:

A large dataset of financial news headlines (over 1.4 million entries)
Historical stock data for 7 major tech companies
Tools like pandas, nltk, pynance, and TA-Lib
📌 Overview
This repository contains Python scripts and Jupyter notebooks that perform the following:

Analyze financial news headlines for sentiment (positive, negative, neutral)
Extract technical indicators such as RSI, MACD, Bollinger Bands, and ATR
Investigate correlations between news sentiment and stock price changes
The goal is to understand whether news sentiment has a measurable impact on stock prices and how technical indicators can help identify market trends.


🔍 Key Insights
Financial News Dataset
Total headlines: 1,407,328
Average headline length: 73 characters
Most active publisher: Paul Quintaro (~228k articles)
Articles are mostly published during weekdays, peaking on Thursday
Sentiment breakdown (using NLTK):
Neutral: 66.4%
Positive: 24.2%
Negative: 9.3%
Stock Market Analysis
Companies analyzed:
Apple
Google
Tesla
Amazon
Meta
Microsoft
NVDA
Meta reached its highest closing price ever in July 2024: $534.69
Strongest correlation: Apple & Microsoft (0.98)
Weakest correlation: Tesla & Meta (0.69)
Correlation Between News and Prices
Company	Daily Range	Close Price
Apple	+0.07	-0.10
Google	+0.05	-0.13
Tesla	+0.05	-0.07
Microsoft	+0.07	-0.12
Meta	+0.06	-0.11
NVDA	+0.02	-0.12
Amazon	+0.04	-0.14

Export to Sheets
Conclusion: Sentiment shows very weak positive correlation with daily range and a slightly negative link with closing prices — indicating limited predictive power when used alone.

🛠️ Setup Instructions
Prerequisites
Python 3.8+
pip package manager
Installation
Bash

# Clone the repo
git clone https://github.com/Addisu-Taye/Predicting-Price-Moves-with-News-Sentiment.git
cd predicting-price-moves

# Install dependencies
pip install -r requirements.txt
Note: Installing TA-Lib may require additional steps depending on your OS. See TA-Lib GitHub for instructions.

Run Notebooks
Bash

jupyter notebook
Navigate to the notebooks/ folder and run each notebook sequentially to reproduce the full analysis pipeline.

🧠 Key Findings
Most headlines are neutral, suggesting conservative reporting or lack of strong opinions.
Tech stocks show high inter-correlations, especially Apple and Microsoft.
Meta experienced a sustained upward trend after layoffs in late 2022 and its first dividend announcement in early 2024.
Tesla showed high volatility linked to external events such as Elon Musk's acquisition of Twitter.
Technical indicators like MACD and RSI were effective in identifying bullish/bearish momentum.
Sentiment alone had minimal direct impact on short-term stock prices.
📝 Recommendations
Expand the news dataset beyond 2020 to improve sentiment–price correlation analysis.
Continue using technical indicators for trading decisions in volatile markets.
Publishers should focus on timely coverage of major global economic events.
⚠️ Challenges Faced
Difficulty installing libraries like TA-Lib.
Limited availability of news data after 2020.
Large datasets required processing via Google Colab due to memory constraints.
📄 License
MIT License – see LICENSE for details.

📬 Contact
For questions or collaboration opportunities, contact:
📧 Addisu Taye – addtaye@gmail.com