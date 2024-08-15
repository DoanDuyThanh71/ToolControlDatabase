import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='Thanhdua12@'
)

cursor = db.cursor()

cursor.execute("use DBCPN")
cursor.execute("ALTER DATABASE DBCPN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
count = 0
for table in tables:
    print(table[0])
    count += 1

print(f"Number of tables: {count}")