import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='Thanhdua12@'
)

cursor = db.cursor()

cursor.execute("use DBCPN")
cursor.execute("ALTER DATABASE DBCPN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")

# cursor.execute("SHOW TABLES")
# tables = cursor.fetchall()
# table_count = len(tables)
# print("Number of tables:", table_count)

# for table in tables:
#     print(table[0])





cursor.execute("SELECT * FROM PerformanceEvaluationHR")
employees = cursor.fetchall()

for employee in employees:
    print(employee)
    
db.commit()
db.close()