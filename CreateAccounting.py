import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='Thanhdua12@'
)

cursor = db.cursor()

cursor.execute("use DBCPN")
cursor.execute("ALTER DATABASE DBCPN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")


# Drop bảng Revenue nếu tồn tại
# cursor.execute(''' DROP TABLE IF EXISTS Revenue ''')

# Tạo bảng Transactions: Giao dịch
cursor.execute('''
CREATE TABLE IF NOT EXISTS Revenue (
    RevenueId INT PRIMARY KEY,
    Date DATE NOT NULL,
    Amount BIGINT NOT NULL,
    Foreign key (RevenueId) references Payments(PaymentId)
)
''')


# Drop bảng Reason nếu tồn tại
# cursor.execute('''DROP TABLE IF EXISTS Reason''')

# Tạo bảng Reason: Ly do chi phí
cursor.execute('''
CREATE TABLE IF NOT EXISTS Reason (
    ReasonId INT PRIMARY KEY,
    Description TEXT NOT NULL
)
''')


# Drop bảng ExpenseReports nếu tồn tại
# cursor.execute('''DROP TABLE IF EXISTS ExpenseReports''')

# Tạo bảng ExpenseReports: Báo cáo chi phí
cursor.execute('''
CREATE TABLE IF NOT EXISTS ExpenseReports (
    ReportId INT PRIMARY KEY,
    ReportDate DATE NOT NULL,
    TotalAmount DECIMAL(10, 2) NOT NULL,
    EmployeeID INT,
    ReasonId INT NOT NULL,
    FOREIGN KEY (EmployeeId) REFERENCES Employee(EmployeeId),
    Foreign key (ReasonId) references Reason(ReasonId)
)
''')

# cursor.execute('''DROP TABLE IF EXISTS PersonalIncomeTax''')

# Tạo bảng PersonalIncomeTax: Thuế thu nhập cá nhân
cursor.execute('''
CREATE TABLE IF NOT EXISTS PersonalIncomeTax (
    PersonalIncomeTaxId INT PRIMARY KEY,
    TaxType  INT NOT NULL,
    INDEX idx_TaxType (TaxType),
    Foreign key (PersonalIncomeTaxId) references Employee(EmployeeId)
)
''')

# cursor.execute('''DROP TABLE IF EXISTS TaxTypeDescription''')

# Tạo bảng TaxTypeDescription: Mô tả loại miễn giảm thuế
cursor.execute('''

CREATE TABLE IF NOT EXISTS TaxTypeDescription (
    TaxTypeID INT PRIMARY KEY,
    Description TEXT NOT NULL,
    FixedTax DECIMAL(10, 2) NOT NULL,
    RateFixedTax INT NOT NULL,
    Foreign key (TaxTypeID) references PersonalIncomeTax(TaxType)
)
''')

# Drop bảng Assets nếu tồn tại
# cursor.execute('''DROP TABLE IF EXISTS Assets''')

# Tạo bảng Assets: Tài sản công ty
cursor.execute('''
CREATE TABLE IF NOT EXISTS Assets (
    AssetId INT PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    Quantity INT NOT NULL,
    UnitPrice DECIMAL(10, 2) NOT NULL
)
''') 

# Tạo bảng Fund với các cột sau: ID, date, Quỹ hoạt động, quỹ dự phòng, quỹ phát triển
cursor.execute('''
CREATE TABLE IF NOT EXISTS Fund (
    FundId INT PRIMARY KEY,
    Date DATE NOT NULL,
    OperatingFund DECIMAL(10, 2) NOT NULL,
    ReserveFund DECIMAL(10, 2) NOT NULL,
    DevelopmentFund DECIMAL(10, 2) NOT NULL
)
''')

# Tạo bảng Receivables: Ghi chép công nợ phải thu
cursor.execute('''
CREATE TABLE IF NOT EXISTS Receivables (
    ReceivablesId INT PRIMARY KEY,
    Date DATE NOT NULL,
    CustomerId INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    DueDate DATE NOT NULL,
    Foreign key (CustomerId) references Customers(CustomerId)
)
''')

# Drop bảng Payables nếu tồn tại
# cursor.execute('''DROP TABLE IF EXISTS Payables''')

# Tạo bảng Payables: Ghi chép công nợ phải trả
cursor.execute('''
CREATE TABLE IF NOT EXISTS Payables (
    PayablesId INT PRIMARY KEY,
    Date DATE NOT NULL,
    CustomerId INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    DueDate DATE NOT NULL,
    Foreign key (CustomerId) references Customers(CustomerId)
)
''')

# Tạo bảng Taxes: Thuế
cursor.execute('''
CREATE TABLE IF NOT EXISTS Taxes (
    TaxId INT PRIMARY KEY,
    Date DATE NOT NULL,
    BusinessTax DECIMAL(10, 2) NOT NULL,
    IncomeTax DECIMAL(10, 2) NOT NULL,
    ValueAddedTax DECIMAL(10, 2) NOT NULL,
    PersonalIncomeTax DECIMAL(10, 2) NOT NULL
)
''')

db.commit()
db.close()
