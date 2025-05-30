# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Page setup
st.set_page_config(
    page_title="News Sentiment & Stock Dashboard",
    layout="wide"
)

st.title("📈 Predicting Price Moves with News Sentiment")

# --- Sidebar ---
st.sidebar.header("Navigation")
section = st.sidebar.radio("Go to", ["📊 EDA Overview", "📰 Sentiment Explorer", "📈 Stock Trends", "ℹ️ About"])

# --- Load data ---
@st.cache_data
def load_data():
    sentiment_path = "data/cleaned_data/cleaned_analyst_ratings.csv"
    stock_path = "data/cleaned_data/cleaned_stock_data.csv"  # Optional

    sentiment_df = pd.read_csv(sentiment_path, parse_dates=True)
    stock_df = pd.read_csv(stock_path, parse_dates=["Date"]) if os.path.exists(stock_path) else None
    return sentiment_df, stock_df

sentiment_df, stock_df = load_data()

# --- EDA Overview ---
if section == "📊 EDA Overview":
    st.subheader("Sentiment Label Distribution")
    col1, col2 = st.columns(2)

    with col1:
        st.write("Sentiment Counts")
        st.dataframe(sentiment_df['sentiment'].value_counts().to_frame())

    with col2:
        fig, ax = plt.subplots()
        sentiment_df['sentiment'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

    st.subheader("Top Tickers & Firms")
    col3, col4 = st.columns(2)

    with col3:
        top_tickers = sentiment_df['ticker'].value_counts().head(10)
        st.bar_chart(top_tickers)

    with col4:
        top_firms = sentiment_df['firm'].value_counts().head(10)
        st.bar_chart(top_firms)

# --- Sentiment Explorer ---
elif section == "📰 Sentiment Explorer":
    st.subheader("Explore Analyst Ratings Sentiment")
    ticker = st.selectbox("Select a Ticker", sentiment_df['ticker'].dropna().unique())

    filtered = sentiment_df[sentiment_df['ticker'] == ticker]

    st.write(f"Showing {len(filtered)} records for {ticker}")
    st.dataframe(filtered)

    st.write("Sentiment by Firm")
    st.bar_chart(filtered['firm'].value_counts())

# --- Stock Trends ---
elif section == "📈 Stock Trends":
    st.subheader("Stock Price & Volume")

    if stock_df is not None:
        selected = st.selectbox("Select a Stock", stock_df['Ticker'].unique())

        df = stock_df[stock_df['Ticker'] == selected]
        df['Date'] = pd.to_datetime(df['Date'])

        st.line_chart(df.set_index('Date')[['Close']])
        st.line_chart(df.set_index('Date')[['Volume']])
    else:
        st.warning("No stock price data found in 'data/cleaned_data/cleaned_stock_data.csv'")

# --- About ---
elif section == "ℹ️ About":
    st.markdown("""
    ### Project: Predicting Price Moves with News Sentiment  
    Developed as part of the 10 Academy Challenge.

    **Modules included:**
    - Raw data cleaning
    - Exploratory data analysis (EDA)
    - Sentiment analysis from analyst ratings
    - Stock price visualization

   Addisu Taye 2025
    """)

