# Filter by Last Online Time

This Python script processes Excel files containing user data and filters entries based on their last online time. It specifically:

1. Reads an Excel file containing user profile data
2. Converts relative time descriptions (e.g., "2 hours ago", "1 day ago") to datetime objects
3. Filters entries based on a 24-hour threshold
4. Removes entries with blank addresses
5. Saves the filtered data to a CSV file

## Requirements

- Python 3.x
- pandas
- openpyxl (for Excel file support)

## Usage

1. Place your Excel file in the same directory as the script
2. Update the input file path in the script if needed
3. Run the script:
```bash
python filter_lastOnline.py
```

The filtered results will be saved to `filtered_lastOnline.csv` in the same directory as the script.

## Features

- Handles various relative time formats (minutes, hours, days, weeks, months, years)
- Converts all timestamps to consistent datetime format
- Filters out entries older than 24 hours
- Removes entries with missing addresses
- Preserves data in CSV format for easy access