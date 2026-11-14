import sqlite3
import pandas as pd

# Connect to the SQLite database and perform operations
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Rename table CarSharing
c.execute("ALTER TABLE CarSharing RENAME TO CarSharing_2")
conn.commit()

# Create table CarSharing and copy necessary columns from CarSharing_2
c.execute("""CREATE TABLE IF NOT EXISTS CarSharing AS SELECT id, timestamp, season, holiday, 
workingday, weather, humidity, windspeed, demand, temp_category FROM CarSharing_2""")
conn.commit()

# Drop the old CarSharing_2 table
c.execute("DROP TABLE IF EXISTS CarSharing_2")
conn.commit()

# Check if table CarSharing has been updated successfully
c.execute("SELECT * FROM CarSharing")
table = c.fetchall()
c.execute("PRAGMA table_info(CarSharing)")
columns = [column[1] for column in c.fetchall()]

# Close the database connection
conn.close()

# Convert the fetched data into a pandas DataFrame
df = pd.DataFrame(table, columns=columns)

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Apply the center alignment style to each individual cell in the DataFrame
styled_df = df.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame
styled_df
