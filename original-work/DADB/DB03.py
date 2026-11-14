# FIRST CELL 

# Import necessary libraries
import sqlite3
import pandas as pd

# Establish database connection
conn = sqlite3.connect('CarSharingDB.db')

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Step 1: Drop the existing CarSharing table if it exists
drop_table_query = """
DROP TABLE IF EXISTS CarSharing;
"""
conn.execute(drop_table_query)

# Step 2: Create table schema
create_table_query = """
CREATE TABLE CarSharing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    user_id INTEGER,
    car_id INTEGER,
    rental_duration_hours REAL,
    pickup_location TEXT,
    dropoff_location TEXT,
    distance_km REAL
);
"""

# Execute the create table query
conn.execute(create_table_query)

# Step 3: Import data into the created table named "CarSharing"
csv_file_path = r'C:\Users\Jyothesh karnam\Desktop\DataBases\CarSharing.csv'
car_data = pd.read_csv(csv_file_path)  # Load data from CSV into a DataFrame
car_data.to_sql('CarSharing', conn, if_exists='replace', index=False)  # Write DataFrame to SQLite table

# Step 4: Check if backup table exists, drop it if it does
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS CarSharingBackup;")
cursor.close()

# Create a backup table and copy data
backup_query = """
CREATE TABLE CarSharingBackup AS 
SELECT * FROM CarSharing;
"""
conn.execute(backup_query)

# Commit changes
conn.commit()

# Now, let's view the entire contents of the CarSharing table
# Fetch the table into a pandas DataFrame
query = "SELECT * FROM CarSharing;"
data = pd.read_sql(query, conn)

# Convert timestamp column to datetime format and format it to display both date and time
data['timestamp'] = pd.to_datetime(data['timestamp']).dt.strftime('%d/%m/%Y %H:%M')

# Apply the center alignment style to each individual cell in the DataFrame
styled_data = data.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',  # apply to all headers
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame
styled_data
  # # SECOND CELL

# # Define the function to categorize temperature
# def categorize_temperature(temp_feel):
#     return 'Cold' if temp_feel < 10 else 'Mild' if 10 <= temp_feel <= 25 else 'Hot'

# # Fetch the data from the CarSharing table
# query = "SELECT id, temp_feel FROM CarSharing;"  # Only select columns needed
# data = pd.read_sql(query, conn)

# # Apply the categorization function to the 'temp_feel' column
# data['temp_category'] = data['temp_feel'].apply(categorize_temperature)

# # Add the 'temp_category' column to the 'CarSharing' table if it doesn't already exist
# try:
#     conn.execute("ALTER TABLE CarSharing ADD COLUMN temp_category TEXT;")
# except sqlite3.OperationalError:
#     # If the column already exists, this error will be caught
#     print("Column 'temp_category' already exists.")

# # Update the CarSharing table with the 'temp_category' values from the DataFrame
# for index, row in data.iterrows():
#     update_query = "UPDATE CarSharing SET temp_category = ? WHERE id = ?;"
#     conn.execute(update_query, (row['temp_category'], row['id']))

# # Commit the changes to the database
# conn.commit()

# # Optionally, fetch and display the updated table to verify the changes
# updated_query = "SELECT * FROM CarSharing;"
# updated_data = pd.read_sql(updated_query, conn)

# # Convert timestamp column to datetime format and format it to display both date and time
# updated_data['timestamp'] = pd.to_datetime(updated_data['timestamp']).dt.strftime('%d/%m/%Y %H:%M')

# # Apply the center alignment style to each individual cell in the DataFrame
# styled_data = updated_data.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
#     'selector': 'th',
#     'props': [('text-align', 'center')]
# }])

# # Display the styled DataFrame
# styled_data
# # THIRD CELL

# # Step 1: Check if the 'temperature' table exists, drop it if it does to start fresh
# cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS temperature;")
# cursor.close()

# # Step 2: Create the 'temperature' table
# create_temperature_table_query = """
# CREATE TABLE temperature (
#     temp REAL,
#     temp_feel REAL,
#     temp_category TEXT
# );
# """

# # Execute the create table query for the 'temperature' table
# conn.execute(create_temperature_table_query)

# # Step 3: Insert data into the 'temperature' table from the 'CarSharing' table
# insert_temperature_data_query = """
# INSERT INTO temperature (temp, temp_feel, temp_category)
# SELECT temp, temp_feel, temp_category FROM CarSharing;
# """

# # Execute the insert data query
# conn.execute(insert_temperature_data_query)

# # Commit changes to the database
# conn.commit()

# # Optional: Display the contents of the 'temperature' table to verify
# query = "SELECT * FROM temperature;"
# temperature_data = pd.read_sql(query, conn)

# # Apply the center alignment style to each individual cell in the DataFrame
# styled_temperature_data = temperature_data.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
#     'selector': 'th',  # Apply to all headers
#     'props': [('text-align', 'center')]
# }])

# # Display the styled DataFrame
# styled_temperature_data

# # THIRD CELL

# # Step 1: Check if the 'temperature' table exists, drop it if it does to start fresh
# cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS temperature;")
# cursor.close()

# # Step 2: Create the 'temperature' table
# create_temperature_table_query = """
# CREATE TABLE temperature (
#     temp REAL,
#     temp_feel REAL,
#     temp_category TEXT
# );
# """

# # Execute the create table query for the 'temperature' table
# conn.execute(create_temperature_table_query)

# # Step 3: Insert data into the 'temperature' table from the 'CarSharing' table
# insert_temperature_data_query = """
# INSERT INTO temperature (temp, temp_feel, temp_category)
# SELECT temp, temp_feel, temp_category FROM CarSharing;
# """

# # Execute the insert data query
# conn.execute(insert_temperature_data_query)

# # Commit changes to the database
# conn.commit()

# # Optional: Display the contents of the 'temperature' table to verify
# query = "SELECT * FROM temperature;"
# temperature_data = pd.read_sql(query, conn)

# # Apply the center alignment style to each individual cell in the DataFrame
# styled_temperature_data = temperature_data.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
#     'selector': 'th',  # Apply to all headers
#     'props': [('text-align', 'center')]
# }])

# # Display the styled DataFrame
# styled_temperature_data

# # FOURTH CELL

# # Step 1: Create a new table excluding 'temp' and 'temp_feel' columns
# create_temp_table_query = """
# CREATE TABLE IF NOT EXISTS CarSharing_temp AS 
# SELECT id, timestamp, season, holiday, workingday, weather, 
#        humidity, windspeed, demand, temp_category
# FROM CarSharing;
# """

# conn.execute(create_temp_table_query)

# # Step 2: Drop the original CarSharing table
# conn.execute("DROP TABLE CarSharing;")

# # Step 3: Rename the temporary table to CarSharing
# conn.execute("ALTER TABLE CarSharing_temp RENAME TO CarSharing;")

# # Commit changes to the database
# conn.commit()

# # Optional: Display the contents of the updated CarSharing table to verify
# query = "SELECT * FROM CarSharing;"  # Fetch all records
# updated_carsharing_data = pd.read_sql(query, conn)

# # Apply the center alignment style to each individual cell in the DataFrame
# styled_updated_carsharing_data = updated_carsharing_data.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
#     'selector': 'th',  # Apply to all headers
#     'props': [('text-align', 'center')]
# }])

# # Display the styled DataFrame
# styled_updated_carsharing_data
# # FIFTH CELL

# # Step 1: Find distinct weather values and assign a number to each
# query = "SELECT DISTINCT weather FROM CarSharing;"
# distinct_weather = pd.read_sql(query, conn)
# weather_to_code = {weather: code for code, weather in enumerate(distinct_weather['weather'], start=1)}

# # Step 2: Add the 'weather_code' column to the 'CarSharing' table
# try:
#     conn.execute("ALTER TABLE CarSharing ADD COLUMN weather_code INTEGER;")
# except sqlite3.OperationalError:
#     # If the column already exists, this error will be caught
#     print("Column 'weather_code' already exists.")

# # Step 3: Update the 'weather_code' column with the corresponding code for each weather value
# for weather, code in weather_to_code.items():
#     update_query = "UPDATE CarSharing SET weather_code = ? WHERE weather = ?;"
#     conn.execute(update_query, (code, weather))

# # Commit the changes to the database
# conn.commit()

# # Optional: Display rows to verify the new 'weather_code' column
# query = "SELECT * FROM CarSharing;"
# updated_data = pd.read_sql(query, conn)

# # Apply the center alignment style to each individual cell in the DataFrame
# styled_updated_data = updated_data.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
#     'selector': 'th',
#     'props': [('text-align', 'center')]
# }])

# # Display the styled DataFrame
# styled_updated_data


# SIXTH CELL

# Step 1: Create the 'weather' table
create_weather_table_query = """
CREATE TABLE IF NOT EXISTS weather (
    weather TEXT,
    weather_code INTEGER PRIMARY KEY
);
"""

conn.execute(create_weather_table_query)

# Step 2: Insert distinct weather and weather_code pairs into the 'weather' table
# Note: Using INSERT OR IGNORE to avoid duplicate insertion errors
insert_weather_data_query = """
INSERT OR IGNORE INTO weather (weather, weather_code)
SELECT DISTINCT weather, weather_code FROM CarSharing;
"""

conn.execute(insert_weather_data_query)

# Commit the changes to the database
conn.commit()

# Optional: Display the contents of the 'weather' table to verify
query = "SELECT * FROM weather;"
weather_data = pd.read_sql(query, conn)

# Apply the center alignment style to each individual cell in the DataFrame
styled_weather_data = weather_data.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',  # Apply to all headers
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame
styled_weather_data


# SEVENTH CELL

# Modify the CarSharing table to exclude the 'weather' column
create_temp_carsharing_query = """
CREATE TABLE IF NOT EXISTS CarSharing_temp AS 
SELECT id, timestamp, season, holiday, workingday, humidity, 
       windspeed, demand, temp_category, weather_code
FROM CarSharing;
"""
conn.execute(create_temp_carsharing_query)

# Drop the original CarSharing table
conn.execute("DROP TABLE CarSharing;")

# Rename the temporary table to CarSharing
conn.execute("ALTER TABLE CarSharing_temp RENAME TO CarSharing;")

# Commit the changes to the database
conn.commit()

# Display the updated CarSharing table
print("\nUpdated CarSharing Table:")
updated_carsharing_data = pd.read_sql("SELECT * FROM CarSharing;", conn)
styled_updated_carsharing_data = updated_carsharing_data.style.set_properties(**{'text-align': 'center'}).set_table_styles([dict(selector='th', props=[('text-align', 'center')])])

styled_updated_carsharing_data

