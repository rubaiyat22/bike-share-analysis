import pandas as pd
import glob

# 1. Load the Data
# Path to the data folder
path = './data'
files = glob.glob(path + "/*.csv")

# Load all CSV files into a single DataFrame
df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)

# 2. Check the Data for Errors
# Check for missing values in key columns
print("Missing values per column:\n", df.isnull().sum())

# Drop rows with missing critical values
df = df.dropna(subset=['ride_id', 'started_at', 'ended_at', 'user_type'])

# 3. Convert data types
# Convert 'started_at' and 'ended_at' to datetime
df['started_at'] = pd.to_datetime(df['started_at'], errors='coerce', infer_datetime_format=True)
df['ended_at'] = pd.to_datetime(df['ended_at'], errors='coerce', infer_datetime_format=True)

# Convert 'rideable_type' to a category type
df['rideable_type'] = df['rideable_type'].astype('category')

# Rename 'member_casual' to 'user_type' for clarity (already renamed)
# df.rename(columns={'member_casual': 'user_type'}, inplace=True)

# 4. Create ride_length, day_of_week, and hour_of_day columns:
# Calculate the ride length in seconds
df['ride_length'] = (df['ended_at'] - df['started_at']).dt.total_seconds()

# Add day of the week (1 = Sunday, 7 = Saturday)
df['day_of_week'] = df['started_at'].dt.weekday + 1

# Add hour of the day for additional analysis
df['hour_of_day'] = df['started_at'].dt.hour

# 5. Handle Outliers in Ride Length:
# Remove rides with negative or very long durations
df = df[df['ride_length'] > 0]
df = df[df['ride_length'] < 86400]  # 24 hours in seconds

# 6. Verify data integrity
# Verify the data types and view the first few rows
print("Data types after cleaning:\n", df.info())
print("First few rows of the cleaned data:\n", df.head())

# 7. Save the Cleaned Data
df.to_csv('./data/cleaned_bike_data.csv', index=False)


### PRINT OUTPUT #####
# Data columns (total 19 columns):
#  #   Column              Dtype
# ---  ------              -----
#  0   ride_id             object
#  1   rideable_type       category
#  2   started_at          datetime64[ns]
#  3   ended_at            datetime64[ns]
#  4   start_station_name  object
#  5   start_station_id    object
#  6   end_station_name    object
#  7   end_station_id      object
#  8   start_lat           float64
#  9   start_lng           float64
#  10  end_lat             float64
#  11  end_lng             float64
#  12  member_casual       object
#  13  user_type           object
#  14  user_type.1         float64
#  15  ride_duration       float64
#  16  day_of_week         int32
#  17  ride_length         float64
#  18  hour_of_day         int32
# dtypes: category(1), datetime64[ns](2), float64(7), int32(2), object(7)
# memory usage: 264.8+ MB
# Data types after cleaning:
#  None
# First few rows of the cleaned data:
#                    ride_id  rideable_type  ... ride_length hour_of_day
# 2990062  743252713F32516B   classic_bike  ...       275.0          19
# 2990063  BE90D33D2240C614  electric_bike  ...       177.0           6
# 2990064  D47BBDDE7C40DD61   classic_bike  ...       978.0          11
# 2990065  6684E760BF9EA9B5   classic_bike  ...       226.0          18
# 2990066  CA9EFC0D24C24A27  electric_bike  ...      2242.0          19

# [5 rows x 19 columns]