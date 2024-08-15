import sqlite3

# Connect to the database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Define the data to be inserted
data = ('John Doe', 25, 'john.doe@example.com')

# Execute the INSERT statement
cursor.execute('INSERT INTO your_table (name, age, email) VALUES (?, ?, ?)', data)

# Commit the changes and close the connection
conn.commit()
conn.close()