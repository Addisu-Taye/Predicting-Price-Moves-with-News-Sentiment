import pandas as pd
import os

# Load the CSV file
file_path = 'sentiment_output.csv'
data = pd.read_csv(file_path)

# Get unique stock tickers
unique_stocks = data['stock'].unique()

# Define the output directory
output_directory = 'Ticker_data'

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through each unique stock ticker and save the corresponding data to a new CSV file
for stock in unique_stocks:
    # Filter the data for the current stock
    stock_data = data[data['stock'] == stock]
    
    # Define the output file name
    output_file = os.path.join(output_directory, f'{stock}_data.csv')
    
    # Save the filtered data to a new CSV file
    stock_data.to_csv(output_file, index=False)

    print(f'Saved data for stock {stock} to {output_file}')