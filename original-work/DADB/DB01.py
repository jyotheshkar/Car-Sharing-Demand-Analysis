#task 1

import sqlite3
import pandas as pd

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Step 1: Create SQLite database
conn = sqlite3.connect('CarSharingDB.db')

# Step 2: Import data into a table named "CarSharing"
csv_file_path = r'C:\Users\Jyothesh karnam\Desktop\DataBases\CarSharing.csv'
car_data = pd.read_csv(csv_file_path)  # Load data from CSV into a DataFrame
car_data.to_sql('CarSharing', conn, if_exists='replace', index=False)  # Write DataFrame to SQLite table

# Step 3: Check if backup table exists, drop it if it does
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

# Close connection
conn.close()

print("Database created, data imported, and backup table created successfully.")

# Now, let's view the entire contents of the CarSharing table
# Reconnect to the SQLite database
conn = sqlite3.connect('CarSharingDB.db')

# Use pandas to query the database and display the entire CarSharing table
query = "SELECT * FROM CarSharing;"
data = pd.read_sql(query, conn)
conn.close()

# Convert timestamp column to datetime format and format it to display both date and time
data['timestamp'] = pd.to_datetime(data['timestamp']).dt.strftime('%d/%m/%Y %H:%M')

# Apply the center alignment style to each individual cell in the DataFrame
styled_data = data.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',  # apply to all headers
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame
styled_data



