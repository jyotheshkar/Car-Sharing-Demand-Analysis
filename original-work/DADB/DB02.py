
# task 2 
import sqlite3
import pandas as pd

# Set pandas display options to show all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Reconnect to the SQLite database
conn = sqlite3.connect('CarSharingDB.db')

# Fetch the table into a pandas DataFrame
query = "SELECT * FROM CarSharing;"
data = pd.read_sql(query, conn)

# Define a function to categorize the 'temp_feel' temperature
def categorize_temperature(temp_feel):
    if temp_feel < 10:
        return 'Cold'
    elif 10 <= temp_feel <= 25:
        return 'Mild'
    else:
        return 'Hot'

# Apply the categorization function to the 'temp_feel' column
data['temp_category'] = data['temp_feel'].apply(categorize_temperature)

# Drop the existing table and recreate it to update the structure and data
data.to_sql('CarSharing', conn, if_exists='replace', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()

# Reapply the styling from Task 1 and display the styled DataFrame
# Convert 'timestamp' column to datetime format and format it to display both date and time, if applicable
data['timestamp'] = pd.to_datetime(data.get('timestamp', pd.Series())).dt.strftime('%d/%m/%Y %H:%M')

# Apply the center alignment style to each individual cell in the DataFrame
styled_data = data.style.set_properties(**{'text-align': 'center'}).set_table_styles([{
    'selector': 'th',
    'props': [('text-align', 'center')]
}])

# Display the styled DataFrame
styled_data
