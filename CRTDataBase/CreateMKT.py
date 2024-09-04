import mysql.connector


db = mysql.connector.connect(
    host='localhost', user='root', password='Thanhdua12@'
)

cursor = db.cursor()

cursor.execute("use DBCPN")
cursor.execute("ALTER DATABASE DBCPN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")


cursor.execute('''
CREATE TABLE IF NOT EXISTS Campaign (
    CampaignId INT UNSIGNED PRIMARY KEY,
    Marketer INT UNSIGNED NOT NULL,
    Name NVARCHAR(63) NOT NULL,
    Brand NVARCHAR(63) NOT NULL,
    Target NVARCHAR(63) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    Description NVARCHAR(255),
    Impression INT UNSIGNED NOT NULL,
    Reach INT UNSIGNED NOT NULL,
    Click INT UNSIGNED NOT NULL,
    Share INT UNSIGNED NOT NULL,
    Cmt INT UNSIGNED NOT NULL,
    Inbox INT UNSIGNED NOT NULL,
    Budget DECIMAL(12,1) NOT NULL,
    fOREIGN KEY (Marketer) REFERENCES Employee(EmployeeId) ON Delete CASCADE On UPDATE CASCADE 
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Leads (
    LeadsId INT UNSIGNED PRIMARY KEY,
    Name NVARCHAR(255) NOT NULL,
    Address NVARCHAR(255) NOT NULL,
    Phone NVARCHAR(15)  NOT NULL,
    Email NVARCHAR(63) NOT NULL,
    Age INT UNSIGNED NOT NULL,
    Gender ENUM('Male', 'Female') NOT NULL,
    Date DATE NOT NULL,
    CampaignId INT UNSIGNED NOT NULL,
    Status NVARCHAR(255)  NOT NULL,
    Score INT UNSIGNED NOT NULL,
    FOREIGN KEY (CampaignId) REFERENCES Campaign(CampaignId) ON Delete CASCADE On UPDATE CASCADE 
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS PageView (
    PageViewId INT UNSIGNED PRIMARY KEY,
    Date DATE NOT NULL,
    Page NVARCHAR(255) NOT NULL,
    PageViews INT UNSIGNED NOT NULL,
    BounceRate INT UNSIGNED NOT NULL,
    AvgTimeOnPage FLOAT NOT NULL,
    Likes INT UNSIGNED NOT NULL,
    Comments INT UNSIGNED NOT NULL,
    Shares INT UNSIGNED NOT NULL
)
''')
# Create a table containing the SEO data: SEOId, Creator, Platform, KeywordRanking, WebTraffic, OrganicKeywordCount, ConversionCount, ExitRate, LinkCount
cursor.execute('''
CREATE TABLE IF NOT EXISTS SEO (
    SEOId INT UNSIGNED PRIMARY KEY,
    Date Date NOT NULL,
    Creator INT UNSIGNED NOT NULL,
    Platform NVARCHAR(63) NOT NULL,
    KeywordRanking INT UNSIGNED NOT NULL,
    WebTraffic INT UNSIGNED NOT NULL,
    OrganicKeywordCount INT UNSIGNED NOT NULL,
    ConversionCount INT UNSIGNED NOT NULL,
    ExitRate FLOAT NOT NULL,
    LinkCount INT UNSIGNED NOT NULL,
    FOREIGN KEY (Creator) REFERENCES Employee(EmployeeId) ON Delete CASCADE On UPDATE CASCADE 
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS PerformanceEvaluationMKT (
    PerformanceEvaluationMKTId INT UNSIGNED PRIMARY KEY,
    EmployeeId INT UNSIGNED NOT NULL,
    Date DATE NOT NULL,
    WorkPerformanceScore INT UNSIGNED NOT NULL,
    ConsciousnessScore INT UNSIGNED NOT NULL,
    LeadCount INT UNSIGNED NOT NULL,
    PageViews INT UNSIGNED NOT NULL,
    BounceRate INT UNSIGNED NOT NULL,
    AvgTimeOnPage FLOAT NOT NULL,
    Likes INT UNSIGNED NOT NULL,
    Comments INT UNSIGNED NOT NULL,
    Shares INT UNSIGNED NOT NULL,
    KeywordRanking INT UNSIGNED NOT NULL,
    WebTraffic INT UNSIGNED NOT NULL,
    OrganicKeywordCount INT UNSIGNED NOT NULL,
    ConversionCount INT UNSIGNED NOT NULL,
    ExitRate FLOAT NOT NULL,
    LinkCount INT UNSIGNED NOT NULL, 
    FOREIGN KEY (EmployeeId) REFERENCES Employee(EmployeeId) ON Delete CASCADE On UPDATE CASCADE 
)
''')


# Create a table containing the KPI data: KPI, nhân viên, ngày, số lượng lead, số lần xem trang, tỉ lệ thoát, thời gian trung bình trên trang, số lượt thích, số lượt bình luận, số lượt chia sẻ, xếp hạng từ khóa, lưu lượng web, số lượng từ khóa hữu cơ, số lượng chuyển đổi, tỉ lệ thoát, số lượng liên kết
cursor.execute('''
CREATE TABLE IF NOT EXISTS KPIMKT (
    KPIMKTId INT UNSIGNED PRIMARY KEY, 
    EmployeeId INT UNSIGNED NOT NULL,
    Date DATE NOT NULL,
    WorkPerformanceScore INT UNSIGNED NOT NULL,
    ConsciousnessScore INT UNSIGNED NOT NULL,
    LeadCount INT UNSIGNED NOT NULL,
    PageViews INT UNSIGNED NOT NULL,
    BounceRate INT UNSIGNED NOT NULL,
    AvgTimeOnPage FLOAT NOT NULL,
    Likes INT UNSIGNED NOT NULL,
    Comments INT UNSIGNED NOT NULL,
    Shares INT UNSIGNED NOT NULL,
    KeywordRanking INT UNSIGNED NOT NULL,
    WebTraffic INT UNSIGNED NOT NULL,
    OrganicKeywordCount INT UNSIGNED NOT NULL,
    ConversionCount INT UNSIGNED NOT NULL,
    ExitRate FLOAT NOT NULL,
    LinkCount INT UNSIGNED NOT NULL,
    FOREIGN KEY (EmployeeId) REFERENCES Employee(EmployeeId) ON Delete CASCADE On UPDATE CASCADE 
)
''')

db.commit()
db.close()
