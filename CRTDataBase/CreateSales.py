import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='Thanhdua12@'
)

cursor = db.cursor()

cursor.execute("use DBCPN")
cursor.execute("ALTER DATABASE DBCPN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")


# Tạo bảng Products
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    ProductId INT UNSIGNED PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    Description TEXT NOT NULL,
    UnitPrice DECIMAL(12,1) NOT NULL,
    Remaining INT UNSIGNED NOT NULL
)
''')


# Tạo bảng Orders
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    OrderId INT UNSIGNED PRIMARY KEY,
    CustomerId INT UNSIGNED NOT NULL,
    OrderDate DATE NOT NULL,
    ProductID INT UNSIGNED NOT NULL,
    TotalAmount DECIMAL(12,1) NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES Leads(LeadId) ON Delete CASCADE On UPDATE CASCADE 
)
''')

# Tạo bảng Payments
cursor.execute('''
CREATE TABLE IF NOT EXISTS Payments (
    PaymentId INT UNSIGNED PRIMARY KEY,
    OrderId INT UNSIGNED NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(12,1) NOT NULL,
    FOREIGN KEY (OrderId) REFERENCES Orders(OrderId) ON Delete CASCADE On UPDATE CASCADE 
)
''')

# Tạo bảng EmployeePerformance
cursor.execute('''
CREATE TABLE IF NOT EXISTS PerformanceEvaluationSales (
    PerformanceEvaluationId INT UNSIGNED PRIMARY KEY,
    Employee INT UNSIGNED NOT NULL,
    Date DATE NOT NULL,
    WorkPerformanceScore INT UNSIGNED NOT NULL,
    ConsciousnessScore INT UNSIGNED NOT NULL,
    CustomerCount INT UNSIGNED NOT NULL,
    TotalRevenue DECIMAL(12,1) NOT NULL,
    DealClosureRate INT UNSIGNED NOT NULL,
    Foreign KEY (Employee) REFERENCES Employee(EmployeeId) ON Delete CASCADE On UPDATE CASCADE 
)
''')

# Tạo bảng KPI
cursor.execute('''
CREATE TABLE IF NOT EXISTS KPISales (
    KPIId INT UNSIGNED PRIMARY KEY,
    Employee INT UNSIGNED NOT NULL,
    Date DATE NOT NULL,
    WorkPerformanceScore INT UNSIGNED NOT NULL,
    ConsciousnessScore INT UNSIGNED NOT NULL,
    CustomerCount INT UNSIGNED NOT NULL,
    TotalRevenue DECIMAL(12,1) NOT NULL,
    DealClosureRate INT UNSIGNED NOT NULL,
    FOREIGN KEY (Employee) REFERENCES Employee(EmployeeId) ON Delete CASCADE On UPDATE CASCADE 
) 
''')



db.commit()
db.close()
