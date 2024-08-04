import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='Thanhdua12@'
)

cursor = db.cursor()

cursor.execute("use DBCPN")
cursor.execute("ALTER DATABASE DBCPN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")


cursor.execute('''
CREATE TABLE IF NOT EXISTS Campaigns (
    CampaignId INT PRIMARY KEY,
    Name NVARCHAR(64) NOT NULL,
    Brand NVARCHAR(64) NOT NULL,
    Target NVARCHAR(64) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    Description NVARCHAR(255),
    Budget DECIMAL(10, 2) NOT NULL
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Leads (
    LeadId INT PRIMARY KEY,
    Name NVARCHAR(255) NOT NULL,
    Address NVARCHAR(255),
    Phone NVARCHAR(16),
    Email NVARCHAR(64),
    Age INT,
    Sex ENUM('Male', 'Female'),
    Date DATE,
    CampaignId INT NOT NULL,
    Status NVARCHAR(255),
    Score INT,
    FOREIGN KEY (CampaignId) REFERENCES Campaigns(CampaignId)
)
''')





db.commit()
db.close()
