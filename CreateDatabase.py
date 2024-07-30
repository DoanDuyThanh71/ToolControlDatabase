import mysql.connector

db = mysql.connector.connect(
    host = 'localhost', user = 'root', password = 'Thanhdua12@'
)

cursor = db.cursor()

cursor.execute("drop database If  EXISTS HR")
cursor.execute("CREATE DATABASE If NOT EXISTS HR ")
cursor.execute("use HR")
cursor.execute("ALTER DATABASE HR CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")


db.commit()
