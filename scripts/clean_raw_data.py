import pandas as pd
import os

def load_raw_data(file_path: str) -> pd.DataFrame:
    """Load raw analyst ratings data."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return pd.read_csv(file_path)

def clean_analyst_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and normalize analyst ratings DataFrame."""
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Strip whitespace from string columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()

    # Convert date columns
    date_cols = [col for col in df.columns if 'date' in col]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Drop rows missing essential fields
    key_cols = ['ticker', 'firm', 'action']
    df.dropna(subset=key_cols, inplace=True)

    return df.reset_index(drop=True)

def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    """Save cleaned DataFrame to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")

def main():
    raw_path = "data/raw_data/raw_analyst_ratings.csv"
    cleaned_path = "data/cleaned_data/cleaned_analyst_ratings.csv"

    try:
        raw_df = load_raw_data(raw_path)
        cleaned_df = clean_analyst_ratings(raw_df)
        save_cleaned_data(cleaned_df, cleaned_path)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
