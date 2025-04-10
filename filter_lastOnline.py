import pandas as pd
from datetime import datetime, timedelta, timezone
import re
import os

# Function to convert relative time descriptions to datetime objects
def convert_relative_time(time_str):
    now = datetime.now()
    
    # Check if it's a relative time description
    if isinstance(time_str, str) and 'ago' in time_str:
        # Extract the number and unit
        match = re.match(r'(\d+)\s+(\w+)\s+ago', time_str)
        if match:
            number, unit = match.groups()
            number = int(number)
            
            # Convert to timedelta
            if 'minute' in unit:
                return now - timedelta(minutes=number)
            elif 'hour' in unit:
                return now - timedelta(hours=number)
            elif 'day' in unit:
                return now - timedelta(days=number)
            elif 'week' in unit:
                return now - timedelta(weeks=number)
            elif 'month' in unit:
                return now - timedelta(days=number*30)  # Approximation
            elif 'year' in unit:
                return now - timedelta(days=number*365)  # Approximation
    
    # If it's not a relative time or the format is unknown, try standard parsing
    try:
        return pd.to_datetime(time_str)
    except:
        return pd.NaT  # Not a Time - pandas' version of NaN for datetime

def main():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the input file path - user should place the Excel file in the same directory
    input_file = os.path.join(script_dir, 'Profile.xlsx')  # Update this filename as needed
    
    # Use read_excel for .xlsx files
    df = pd.read_excel(input_file)
    
    # Convert the 'Last Online Time' column to datetime using our custom function
    df['Last Online Time'] = df['Last Online Time'].apply(convert_relative_time)
    
    # Make one_day_ago timezone-aware with UTC
    one_day_ago = (datetime.now(timezone.utc) - timedelta(days=1))
    filtered_df = df[df['Last Online Time'] <= one_day_ago]
    
    # Construct the full path for the output file
    output_file_path = os.path.join(script_dir, 'filtered_lastOnline.csv')
    
    # Save the filtered data
    filtered_df.to_csv(output_file_path, index=False)
    
    # Read the filtered CSV file
    filtered_df = pd.read_csv(output_file_path)
    
    # Filter out rows where the address column is blank or NaN
    filtered_df = filtered_df.dropna(subset=['Address'])
    
    # Save the filtered data back to the CSV file
    filtered_df.to_csv(output_file_path, index=False)

if __name__ == "__main__":
    main()