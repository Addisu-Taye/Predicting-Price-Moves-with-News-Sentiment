import pandas as pd
import os

def load_data(file_path: str) -> pd.DataFrame:
    """Load raw CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    return pd.read_csv(file_path)

def clean_generic_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and normalize generic CSV data with reporting."""

    original_rows = len(df)
    print(f"📥 Original rows: {original_rows}")

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    print("📌 Columns after cleaning:", df.columns.tolist())

    # Strip whitespace from string columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].str.strip()

    # Convert 'date' to datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Drop duplicates
    before_dedup = len(df)
    df.drop_duplicates(inplace=True)
    after_dedup = len(df)
    print(f"🗑️ Duplicates removed: {before_dedup - after_dedup}")

    # Drop rows with missing required fields
    required = ['date', 'stock']
    before_dropna = len(df)
    df.dropna(subset=[col for col in required if col in df.columns], inplace=True)
    after_dropna = len(df)
    print(f"⚠️ Rows dropped due to missing 'date' or 'stock': {before_dropna - after_dropna}")

    final_rows = len(df)
    print(f"✅ Final cleaned rows: {final_rows} (removed {original_rows - final_rows})")

    return df.reset_index(drop=True)

def save_cleaned_data(df: pd.DataFrame, output_path: str) -> None:
    """Save cleaned DataFrame to CSV."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"💾 Cleaned data saved to: {output_path}")

def main():
    input_path = "data/raw_data/raw_analyst_ratings.csv"
    output_path = "data/cleaned_data/cleaned_analyst_ratings.csv"

    try:
        raw_df = load_data(input_path)
        cleaned_df = clean_generic_data(raw_df)
        save_cleaned_data(cleaned_df, output_path)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
