import pandas as pd

import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='Thanhdua12@'
)

cursor = db.cursor()

cursor.execute("use DBCPN")
cursor.execute("ALTER DATABASE DBCPN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")

def delete_department_data():
    db = mysql.connector.connect(
        host='localhost', user='root', password='Thanhdua12@'
    )
    cursor = db.cursor()
    cursor.execute("use DBCPN")
    
    
    # Delete all data from the Department table
    cursor.execute("DELETE FROM Department")
    db.commit()
    
    # Close the database connection
    db.close()
    
    
delete_department_data()
# Read data from Excel file
data = pd.read_excel('template Excel/HR/Department.xlsx')

# Iterate over each row in the data
for index, row in data.iterrows():
    department_name = row['DepartmentName']
    
    # Insert department data into the table
    cursor.execute("INSERT INTO Department (DepartmentName) VALUES (%s)", (department_name,))
    db.commit()


    # Retrieve department data from the table
    cursor.execute("SELECT * FROM Department")
    departments = cursor.fetchall()

    # Print the department data
    for department in departments:
        print(department)

    # Close the database connection
db.close()


