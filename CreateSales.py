import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='Thanhdua12@'
)

cursor = db.cursor()

cursor.execute("use DBCPN")
cursor.execute("ALTER DATABASE DBCPN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")


# cursor.execute("DROP TABLE IF EXISTS Campaigns")

# Tạo bảng Customers với các cột mới
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    CustomerId INT PRIMARY KEY,
    Campaign INT NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES Leads(LeadId)
)
''')

# Tạo bảng Orders
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    OrderId INT PRIMARY KEY,
    CustomerId INT NOT NULL,
    OrderDate DATE NOT NULL,
    TotalAmount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId)
)
''')

# Tạo bảng Products
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    ProductId INT PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL,
    remaining INT NOT NULL
)
''')



# Tạo bảng OrderDetails
cursor.execute('''
CREATE TABLE IF NOT EXISTS OrderDetails (
    OrderDetailId INT PRIMARY KEY,
    CustomerId INT NOT NULL,
    OrderId INT NOT NULL,
    ProductId INT NOT NULL,
    Quantity INT NOT NULL,
    FOREIGN KEY (OrderId) REFERENCES Orders(OrderId),
    FOREIGN KEY (ProductId) REFERENCES Products(ProductId),
    Foreign KEY (CustomerId) REFERENCES Customers(CustomerId)
)
''')

# Tạo bảng Payments
cursor.execute('''
CREATE TABLE IF NOT EXISTS Payments (
    PaymentId INT PRIMARY KEY,
    OrderId INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (OrderId) REFERENCES Orders(OrderId)
)
''')




db.commit()
db.close()
