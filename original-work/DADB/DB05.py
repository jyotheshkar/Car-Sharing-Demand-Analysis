

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Fetch and display the full 'weather' table
c.execute("SELECT * FROM weather")
weather_data = c.fetchall()
weather_df = pd.DataFrame(weather_data, columns=['weather', 'weather_code'])

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Apply the center alignment style to each individual cell in the DataFrame
styled_weather_df = weather_df.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame for the 'weather' table
print("\nData in 'weather' table:")
display(styled_weather_df)

# Fetch and display the full 'CarSharing' table to verify the 'weather' column is dropped and 'weather_code' is present
c.execute("SELECT * FROM CarSharing")
carsharing_data = c.fetchall()
# Assuming you know the column names since 'PRAGMA table_info(CarSharing)' was used before
carsharing_columns = ['id', 'timestamp', 'season', 'holiday', 'workingday', 'humidity', 'windspeed', 'demand', 'temp_category', 'weather_code']
carsharing_df = pd.DataFrame(carsharing_data, columns=carsharing_columns)

# Apply the center alignment style to the 'CarSharing' DataFrame
styled_carsharing_df = carsharing_df.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame for the 'CarSharing' table
print("\nData in 'CarSharing' table:")
display(styled_carsharing_df)

# Close the database connection
conn.close()
