# Bike Share Analysis

## Overview

This project analyzes bike-share usage data to understand how casual riders and annual members use Cyclistic bikes differently. By exploring metrics like ride frequency, ride duration, and bike type preferences, the goal is to provide insights that can help Cyclistic's marketing team target casual riders and encourage them to convert to annual memberships.

## Data Setup

Due to file size limitations, the necessary data files are not included in this repository. To set up the data:

1. **Download the Data**: Download the required CSV files from the official Cyclistic bike-share data repository - https://divvy-tripdata.s3.amazonaws.com/index.html.
2. **Create `/data` Folder**: Create a folder named `data` in the project’s root directory.
3. **Move Data Files**: Place all downloaded CSV files into the `data` folder.

Once the data is in place, the analysis can be performed.

## Data format

The data used in this analysis comes from Cyclistic's bike-share system, consisting of multiple CSV files representing bike ride data for several months. The key attributes include:

- Ride ID
- Bike type
- Start and end timestamps
- Member status (casual or annual)
- Station details

## Files

- `analyze_data.py`: Contains the code for data analysis, including calculating ride frequency, duration, and bike type preferences.
- `load_and_process_data.py`: Loads and processes the raw data, ensuring it is clean and ready for analysis.
- `presentation.md`: A markdown file presenting key insights and recommendations based on the analysis.
- `viz`: Contains visualizations created during the analysis.

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/rubaiyat22/bike-share-analysis.git
    ```
2. Install the required dependencies:
    ```
    pip install pandas matplotlib seaborn
    ```

3. Run the process and analysis script:
    ```
    python load_and_process_data.py
    python analyze_data.py
    ```
    
## Key Insights

- Casual riders tend to ride on weekends and prefer electric bikes slightly more than classic bikes.
- Annual members have more consistent usage throughout the week, favoring classic bikes.
- Recommendations include promoting longer rides for casual riders, creating weekend promotions, and reallocating bike fleets based on user preferences.

More detailed findinings are in presentation.md

