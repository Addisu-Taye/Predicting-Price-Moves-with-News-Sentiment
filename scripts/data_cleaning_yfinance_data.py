import pandas as pd

def clean_and_report_data(file_path, output_file_path="cleaned_historical_data.csv"):
    """
    Cleans historical stock data by handling missing values, duplicates,
    and ensuring correct data types. Reports cleaning actions and saves
    the cleaned data.

    Args:
        file_path (str): The path to the input CSV file (e.g., 'TSLA_historical_data.csv').
        output_file_path (str): The path to save the cleaned CSV file.
    """
    print(f"--- Data Cleaning Report for {file_path} ---")

    try:
        # Load the dataset
        df = pd.read_csv(file_path)
        print(f"Initial data shape: {df.shape[0]} rows, {df.shape[1]} columns")

        # --- Cleaning Type 1: Handling Duplicate Rows ---
        initial_rows = df.shape[0]
        df.drop_duplicates(inplace=True)
        duplicates_removed = initial_rows - df.shape[0]
        print(f"Cleaning Type: Duplicate Rows Removal")
        print(f"  Number of duplicate rows removed: {duplicates_removed}")

        # --- Cleaning Type 2: Handling Missing Values ---
        # Identify missing values before any action
        missing_before = df.isnull().sum().sum()
        print(f"Cleaning Type: Missing Values Handling")
        print(f"  Total missing values before cleaning: {missing_before}")

        # For financial historical data, missing price/volume can be problematic.
        # It's often best to drop rows with any missing critical data.
        initial_rows_after_duplicates = df.shape[0]
        df.dropna(inplace=True)
        rows_with_missing_dropped = initial_rows_after_duplicates - df.shape[0]
        print(f"  Number of rows dropped due to missing values: {rows_with_missing_dropped}")

        # --- Cleaning Type 3: Correcting Data Types ---
        print("Cleaning Type: Data Type Correction")
        # Convert 'Date' column to datetime objects
        original_date_type = df['Date'].dtype
        df['Date'] = pd.to_datetime(df['Date'])
        new_date_type = df['Date'].dtype
        print(f"  'Date' column type changed from {original_date_type} to {new_date_type}")

        # Ensure numerical columns are numeric
        numerical_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
        for col in numerical_cols:
            if col in df.columns:
                original_num_type = df[col].dtype
                # Coerce errors to NaN, then drop NaNs if any arise from conversion
                df[col] = pd.to_numeric(df[col], errors='coerce')
                # Drop rows where numerical conversion resulted in NaN
                if df[col].isnull().any():
                    initial_rows_before_num_drop = df.shape[0]
                    df.dropna(subset=[col], inplace=True)
                    num_conversion_nans_dropped = initial_rows_before_num_drop - df.shape[0]
                    print(f"  Dropped {num_conversion_nans_dropped} rows due to non-numeric values in '{col}'")
                print(f"  '{col}' column type ensured to be numeric (was {original_num_type}, now {df[col].dtype})")
            else:
                print(f"  Warning: Column '{col}' not found in data.")


        # Sort data by date (important for time series analysis like daily returns)
        df.sort_values(by='Date', inplace=True)
        print("  Data sorted by 'Date' column.")

        print(f"\nFinal cleaned data shape: {df.shape[0]} rows, {df.shape[1]} columns")
        print(f"Total rows removed during cleaning: {initial_rows - df.shape[0]}")

        # Save the cleaned data
        df.to_csv(output_file_path, index=False)
        print(f"Cleaned data saved to '{output_file_path}'")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred during cleaning: {e}")

# Example usage:
# Make sure 'TSLA_historical_data.csv' is in the same directory as your script
clean_and_report_data('TSLA_historical_data.csv', 'tsla_cleaned_data.csv')

