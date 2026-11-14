import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect("CarSharingDB.db")
c = conn.cursor()

# Fetch the data from the 'time' table
c.execute("SELECT * FROM time")
time_data = c.fetchall()

# Assuming you know the column names
columns = ['timestamp', 'hour', 'weekday_name', 'month_name']

# Convert the fetched data into a pandas DataFrame
time_df = pd.DataFrame(time_data, columns=columns)

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Apply the center alignment style to each individual cell in the DataFrame
styled_time_df = time_df.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame
print("\nData in 'time' table:")
display(styled_time_df)  # Use display for Jupyter Notebook or IPython environments

# Close the database connection
conn.close()
