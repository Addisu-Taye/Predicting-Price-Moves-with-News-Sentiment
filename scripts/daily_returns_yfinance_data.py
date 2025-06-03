import pandas as pd

def calculate_daily_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the daily percentage return for a stock's historical data.
    The function is generic and expects a DataFrame with at least 'Date' and 'Close' columns.

    Args:
        df (pd.DataFrame): A DataFrame containing historical stock data,
                           expected to have 'Date' and 'Close' columns.

    Returns:
        pd.DataFrame: The input DataFrame with an additional 'Daily_Return' column,
                      representing the daily percentage change in 'Close' price.
                      Returns None if 'Date' or 'Close' columns are missing.
    """
    if 'Date' not in df.columns or 'Close' not in df.columns:
        print("Error: DataFrame must contain 'Date' and 'Close' columns to calculate daily returns.")
        return None

    # Ensure 'Date' is datetime and sort the DataFrame by date
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by='Date', inplace=True)

    # Calculate daily returns using the 'Close' price
    # pct_change() calculates the percentage change from the previous row
    df['Daily_Return'] = df['Close'].pct_change() * 100 # Multiply by 100 for percentage

    return df

# Example usage:
# Assuming 'tsla_cleaned_data.csv' is the output from the cleaning script
try:
    cleaned_df = pd.read_csv('tsla_cleaned_data.csv')
    
    # Calculate daily returns
    df_with_returns = calculate_daily_returns(cleaned_df.copy()) # Use .copy() to avoid SettingWithCopyWarning

    if df_with_returns is not None:
        # Display the first few rows with daily returns
        print("\n--- Daily Returns Calculation ---")
        print("First 5 rows with Daily Returns:")
        print(df_with_returns[['Date', 'Close', 'Daily_Return']].head())

        # Save the DataFrame with daily returns
        output_returns_file = 'tsla_daily_returns.csv'
        df_with_returns.to_csv(output_returns_file, index=False)
        print(f"\nDaily returns data saved to '{output_returns_file}'")
    
except FileNotFoundError:
    print("Error: 'tsla_cleaned_data.csv' not found. Please run the cleaning script first.")
except Exception as e:
    print(f"An error occurred during daily return calculation: {e}")

