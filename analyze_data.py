# 1. Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the cleaned data
df = pd.read_csv('./data/cleaned_bike_data.csv')

# 2. Explore Membership Trends
# Frequency of rides by user type (annual vs casual)
ride_counts = df['user_type'].value_counts()
print(f"Ride counts by user type:\n{ride_counts}")

# 3. Ride Frequency by Day of the Week
df['day_name'] = df['day_of_week'].map({
    1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'
})
ride_frequency_by_day = df.groupby(['day_name', 'user_type']).size().unstack().fillna(0)
ride_frequency_by_day = ride_frequency_by_day[['casual', 'member']]  # Ensure the right order in plot

ride_frequency_by_day.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Ride Frequency by Day of Week (Annual vs Casual)')
plt.xlabel('Day of Week')
plt.ylabel('Number of Rides')
plt.xticks(rotation=45)
plt.show()


# 4. Ride Duration by User Type (Annual vs Casual) in Minutes
# Convert ride length to minutes
df['ride_length_minutes'] = df['ride_length'] / 60  # Convert to minutes
average_ride_duration = df.groupby('user_type')['ride_length_minutes'].mean()

# Plot Ride Duration (in minutes)
average_ride_duration.plot(kind='bar', figsize=(8, 5), color=['orange', 'blue'])
plt.title('Average Ride Duration by User Type (Minutes)')
plt.xlabel('User Type')
plt.ylabel('Average Ride Duration (minutes)')
plt.tight_layout()
plt.show()

# 5. Bike Type Preference by User Type (in Percentage)
# Calculate the percentage distribution of bike types for each user type
bike_type_preference_percentage = (
    df.groupby(['user_type', 'rideable_type']).size()
    .groupby(level=0)  # Group by 'user_type'
    .apply(lambda x: (x / x.sum()) * 100)  # Convert counts to percentages
    .unstack()  # Pivot the table for plotting
    .fillna(0)  # Fill any missing values with 0
)

# Plot Bike Type Preference as a percentage
bike_type_preference_percentage.plot(
    kind='bar',
    figsize=(8, 6),
    color=['blue', 'orange'],  # Colors for bike types
    edgecolor='black'
)

# Customize the plot
plt.title('Bike Type Preference by User Type (in Percentage)')
plt.xlabel('User Type')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)  # Keep x-axis labels horizontal
plt.legend(title='Bike Type', loc='upper left')  # Add legend for bike types
plt.tight_layout()  # Adjust layout
plt.show()
