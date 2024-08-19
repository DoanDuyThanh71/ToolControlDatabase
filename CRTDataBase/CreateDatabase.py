import mysql.connector

db = mysql.connector.connect(
    host = 'localhost', user = 'root', password = 'Thanhdua12@'
)

cursor = db.cursor()

cursor.execute("drop database If  EXISTS DBCPN")
cursor.execute("CREATE DATABASE If NOT EXISTS DBCPN ")
cursor.execute("use DBCPN")
cursor.execute("ALTER DATABASE DBCPN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")


db.commit()
db.close()
