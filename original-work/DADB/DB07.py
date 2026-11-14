# task 7 subtask A

# # 7a

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Execute the query to find the date and time with the highest demand in 2017
c.execute("""
SELECT timestamp, MAX(demand) AS highest_demand
FROM CarSharing
WHERE strftime('%Y', timestamp) = '2017'
""")
highest_demand_2017 = c.fetchall()

# Convert the result to a pandas DataFrame
df_highest_demand_2017 = pd.DataFrame(highest_demand_2017, columns=['timestamp', 'highest_demand'])

# Apply the center alignment style to each individual cell in the DataFrame
styled_df_highest_demand_2017 = df_highest_demand_2017.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame
print("\nDate and time with the highest demand rate in 2017:")
display(styled_df_highest_demand_2017)  # Use display for Jupyter Notebook or IPython environments

# Close the database connection
conn.close()


# task 7 subtask b 

# # 7b


import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Calculate the average demand for each combination of weekday, month, and season in 2017
c.execute("""
SELECT 
    strftime('%w', timestamp) AS weekday,
    strftime('%m', timestamp) AS month,
    season,
    AVG(demand) AS avg_demand
FROM CarSharing
WHERE strftime('%Y', timestamp) = '2017'
GROUP BY weekday, month, season
ORDER BY avg_demand DESC
""")
avg_demand_details_2017 = c.fetchall()

# Convert the query results into a DataFrame
df_avg_demand_details_2017 = pd.DataFrame(avg_demand_details_2017, columns=['weekday', 'month', 'season', 'avg_demand'])

# Identify the highest and lowest average demand rates
highest_avg_demand = df_avg_demand_details_2017.iloc[[0]].assign(Average_Demand_Type='Highest')
lowest_avg_demand = df_avg_demand_details_2017.iloc[[-1]].assign(Average_Demand_Type='Lowest')

# Combine the highest and lowest entries into one DataFrame for display
df_combined = pd.concat([highest_avg_demand, lowest_avg_demand])

# Map the weekday numbers to names
weekday_map = {
    '0': 'Sunday', '1': 'Monday', '2': 'Tuesday', '3': 'Wednesday',
    '4': 'Thursday', '5': 'Friday', '6': 'Saturday'
}
df_combined['weekday'] = df_combined['weekday'].map(weekday_map)

# Map the month numbers to names
month_map = {
    '01': 'January', '02': 'February', '03': 'March', '04': 'April',
    '05': 'May', '06': 'June', '07': 'July', '08': 'August',
    '09': 'September', '10': 'October', '11': 'November', '12': 'December'
}
df_combined['month'] = df_combined['month'].map(month_map)

# Reorder DataFrame columns for better readability
df_combined = df_combined[['Average_Demand_Type', 'weekday', 'month', 'season', 'avg_demand']]

# Apply the center alignment style to each individual cell in the DataFrame
styled_df_combined = df_combined.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame
print("\nWeekday, month, and season with the highest and lowest average demand rates in 2017, including average demand values:")
display(styled_df_combined)

# Close the database connection
conn.close()

#  task 7 subtask c

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Since the highest average demand was on Sundays, we'll use '0' (Sunday's identifier in SQLite's strftime('%w', timestamp))
weekday_chosen = '0'  # '0' for Sunday

# Execute the query to calculate the average demand rate at different hours for Sundays throughout 2017
c.execute("""
SELECT
    strftime('%H', timestamp) AS hour,
    AVG(demand) AS avg_demand
FROM CarSharing
WHERE strftime('%Y', timestamp) = '2017' AND strftime('%w', timestamp) = ?
GROUP BY hour
ORDER BY avg_demand DESC
""", (weekday_chosen,))

hourly_demand_2017 = c.fetchall()

# Close the database connection
conn.close()

# Convert the result to a pandas DataFrame
df_hourly_demand_2017 = pd.DataFrame(hourly_demand_2017, columns=['hour', 'avg_demand'])

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Apply the center alignment style to each individual cell in the DataFrame
styled_df_hourly_demand_2017 = df_hourly_demand_2017.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame
print("\nAverage demand rate at different hours for Sundays throughout 2017:")
styled_df_hourly_demand_2017

# task 7 subtask d 

#  task 7 d 
# Part 1.1: Predominant Weather Condition in 2017

import sqlite3

# Reconnect to the SQLite database
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Query to find the most prevalent temp_category in 2017
c.execute("""
SELECT temp_category, COUNT(temp_category) AS count
FROM CarSharing
WHERE strftime('%Y', timestamp) = '2017'
GROUP BY temp_category
ORDER BY count DESC
LIMIT 1
""")
most_prevalent_temp_category = c.fetchone()

print(f"Most prevalent temperature category in 2017: {most_prevalent_temp_category[0]} (Occurrences: {most_prevalent_temp_category[1]})")

# Close the database connection for this part
conn.close()

#  task 7 d 
# Part 1.2: Predominant Weather Condition in 2017

# Reconnect to the SQLite database
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Assuming a 'weather' table exists that maps 'weather_code' to weather descriptions
c.execute("""
SELECT w.weather, COUNT(*) AS count
FROM CarSharing cs
JOIN weather w ON cs.weather_code = w.weather_code
WHERE strftime('%Y', cs.timestamp) = '2017'
GROUP BY w.weather
ORDER BY count DESC
LIMIT 1
""")
most_prevalent_weather = c.fetchone()

print(f"Most prevalent weather condition in 2017: {most_prevalent_weather[0]} (Occurrences: {most_prevalent_weather[1]})")

# Close the database connection for this part
conn.close()

#  task 7 d 
# Part 1.3

import sqlite3
import pandas as pd

# Reconnect to the SQLite database
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Query to analyze wind speed for each month in 2017
c.execute("""
SELECT 
    strftime('%m', timestamp) AS month,
    AVG(windspeed) AS avg_wind_speed,
    MAX(windspeed) AS max_wind_speed,
    MIN(windspeed) AS min_wind_speed
FROM CarSharing
WHERE strftime('%Y', timestamp) = '2017'
GROUP BY month
ORDER BY month
""")
wind_speed_stats = c.fetchall()

# Close the database connection
conn.close()

# Convert the results to a pandas DataFrame
df_wind_speed_stats = pd.DataFrame(wind_speed_stats, columns=['Month', 'Average Wind Speed', 'Maximum Wind Speed', 'Minimum Wind Speed'])

# Apply the center alignment style to each individual cell in the DataFrame
styled_df_wind_speed_stats = df_wind_speed_stats.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame
print("\nWind Speed Analysis for Each Month in 2017:")
styled_df_wind_speed_stats

#  task 7 d 
# Part 1.4

# Reconnect to the SQLite database for humidity analysis
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Query to analyze humidity for each month in 2017
c.execute("""
SELECT 
    strftime('%m', timestamp) AS month,
    AVG(humidity) AS avg_humidity,
    MAX(humidity) AS max_humidity,
    MIN(humidity) AS min_humidity
FROM CarSharing
WHERE strftime('%Y', timestamp) = '2017'
GROUP BY month
ORDER BY month
""")
humidity_stats = c.fetchall()

# Close the database connection
conn.close()

# Convert the results to a pandas DataFrame
df_humidity_stats = pd.DataFrame(humidity_stats, columns=['Month', 'Average Humidity', 'Maximum Humidity', 'Minimum Humidity'])

# Apply the center alignment style to each individual cell in the DataFrame
styled_df_humidity_stats = df_humidity_stats.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame
print("\nHumidity Analysis for Each Month in 2017:")
styled_df_humidity_stats

#  task 7 d 
# Part 1.5

import sqlite3
import pandas as pd

# Reconnect to the SQLite database
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Query to find the average demand rate for each temp_category in 2017, sorted in descending order of avg_demand
c.execute("""
SELECT 
    temp_category, 
    AVG(demand) AS avg_demand
FROM CarSharing
WHERE strftime('%Y', timestamp) = '2017'
GROUP BY temp_category
ORDER BY avg_demand DESC
""")
avg_demand_by_temp_category = c.fetchall()

# Close the database connection
conn.close()

# Convert the results to a pandas DataFrame
df_avg_demand_by_temp_category = pd.DataFrame(avg_demand_by_temp_category, columns=['Temperature Category', 'Average Demand'])

# Apply the center alignment style to each individual cell in the DataFrame
styled_df_avg_demand_by_temp_category = df_avg_demand_by_temp_category.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame
print("\nAverage Demand Rate for Each Temperature Category in 2017:")
styled_df_avg_demand_by_temp_category


#  task 7 subtask e

import sqlite3
import pandas as pd

# Reconnect to the SQLite database
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Query to find the month with the highest average demand in 2017
c.execute("""
SELECT 
    strftime('%m', timestamp) AS month,
    AVG(demand) AS avg_demand
FROM CarSharing
WHERE strftime('%Y', timestamp) = '2017'
GROUP BY month
ORDER BY avg_demand DESC
LIMIT 1
""")
month_with_highest_demand = c.fetchone()[0]  # Extract just the month part for the next queries

# Close the database connection after fetching the month
conn.close()

print(f"Month with the highest average demand in 2017: {month_with_highest_demand}")


#  additional 

import sqlite3
import pandas as pd

# Reconnect to the SQLite database
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Query to get the average demand for each month in 2017
c.execute("""
SELECT 
    strftime('%m', timestamp) AS month,
    AVG(demand) AS avg_demand
FROM CarSharing
WHERE strftime('%Y', timestamp) = '2017'
GROUP BY month
ORDER BY avg_demand DESC
""")
all_months_avg_demand = c.fetchall()

# Close the database connection
conn.close()

# Convert the results to a pandas DataFrame for better visualization
df_all_months_avg_demand = pd.DataFrame(all_months_avg_demand, columns=['Month', 'Average Demand'])

# Display the DataFrame
print("\nAverage Demand for Each Month in 2017:")
print(df_all_months_avg_demand)

