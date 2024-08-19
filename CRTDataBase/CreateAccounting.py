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
    RevenueId INT UNSIGNED PRIMARY KEY,
    Date DATE NOT NULL,
    Amount DECIMAL(12,1) NOT NULL,
    Foreign key (RevenueId) references Payments(PaymentId)
)
''')


# Drop bảng Reason nếu tồn tại
# cursor.execute('''DROP TABLE IF EXISTS Reason''')

# Tạo bảng Reason: Ly do chi phí
cursor.execute('''
CREATE TABLE IF NOT EXISTS Reason (
    ReasonId INT UNSIGNED PRIMARY KEY,
    Description TEXT NOT NULL
)
''')


# Drop bảng ExpenseReports nếu tồn tại
# cursor.execute('''DROP TABLE IF EXISTS ExpenseReports''')

# Tạo bảng ExpenseReports: Báo cáo chi phí
cursor.execute('''
CREATE TABLE IF NOT EXISTS ExpenseReports (
    ReportId INT UNSIGNED PRIMARY KEY,
    ReportDate DATE NOT NULL,
    TotalAmount DECIMAL(12,1)  NOT NULL,
    EmployeeID INT UNSIGNED,
    ReasonId INT UNSIGNED NOT NULL,
    Status ENUM('Approved', 'Pending', 'Rejected', 'Wrong') NOT NULL,
    AcceptDate DATE NOT NULL,
    FOREIGN KEY (EmployeeId) REFERENCES Employee(EmployeeId),
    Foreign key (ReasonId) references Reason(ReasonId)
)
''')

# Tạo bảng TaxTypeDescription: Mô tả loại miễn giảm thuế
cursor.execute('''

CREATE TABLE IF NOT EXISTS TaxTypeDescription (
    TaxTypeID INT UNSIGNED PRIMARY KEY,
    Description TEXT NOT NULL,
    FixedTax DECIMAL(12,1)  NOT NULL,
    RateFixedTax INT UNSIGNED NOT NULL
)
''')

# cursor.execute('''DROP TABLE IF EXISTS PersonalIncomeTax''')

# Tạo bảng PersonalIncomeTax: Thuế thu nhập cá nhân
cursor.execute('''
CREATE TABLE IF NOT EXISTS PersonalIncomeTax (
    PersonalIncomeTaxId INT UNSIGNED PRIMARY KEY,
    TaxType  INT UNSIGNED NOT NULL,
    Foreign key (PersonalIncomeTaxId) references Employee(EmployeeId),
    Foreign key (TaxType) references TaxTypeDescription(TaxTypeID)
)
''')

# cursor.execute('''DROP TABLE IF EXISTS TaxTypeDescription''')



# Drop bảng Assets nếu tồn tại
# cursor.execute('''DROP TABLE IF EXISTS Assets''')

# Tạo bảng Assets: Tài sản công ty
cursor.execute('''
CREATE TABLE IF NOT EXISTS Assets (
    AssetId INT UNSIGNED PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    Quantity INT UNSIGNED NOT NULL,
    UnitPrice DECIMAL(12,1)  NOT NULL
)
''') 

# Tạo bảng Fund với các cột sau: ID, date, Quỹ hoạt động, quỹ dự phòng, quỹ phát triển
cursor.execute('''
CREATE TABLE IF NOT EXISTS Fund (
    FundId INT UNSIGNED PRIMARY KEY,
    Date DATE NOT NULL,
    OperatingFund DECIMAL(12,1)  NOT NULL,
    ReserveFund DECIMAL(12,1)  NOT NULL,
    DevelopmentFund DECIMAL(12,1)  NOT NULL
)
''')

# Tạo bảng Receivables: Ghi chép công nợ phải thu
cursor.execute('''
CREATE TABLE IF NOT EXISTS Receivables (
    ReceivablesId INT UNSIGNED PRIMARY KEY,
    Date DATE NOT NULL,
    CustomerId INT UNSIGNED NOT NULL,
    Amount DECIMAL(12,1)  NOT NULL,
    DueDate DATE NOT NULL,
    Foreign key (CustomerId) references Leads(LeadId)
)
''')

# Drop bảng Payables nếu tồn tại
# cursor.execute('''DROP TABLE IF EXISTS Payables''')

# Tạo bảng Payables: Ghi chép công nợ phải trả
cursor.execute('''
CREATE TABLE IF NOT EXISTS Payables (
    PayablesId INT UNSIGNED PRIMARY KEY,
    Date DATE NOT NULL,
    CustomerId INT UNSIGNED NOT NULL,
    Amount DECIMAL(12,1)  NOT NULL,
    DueDate DATE NOT NULL,
    Foreign key (CustomerId) references Leads(LeadId)
)
''')

# Tạo bảng Taxes: Thuế
cursor.execute('''
CREATE TABLE IF NOT EXISTS Taxes (
    TaxId INT UNSIGNED PRIMARY KEY,
    Date DATE NOT NULL,
    BusinessTax DECIMAL(12,1)  NOT NULL,
    IncomeTax DECIMAL(12,1)  NOT NULL,
    ValueAddedTax DECIMAL(12,1)  NOT NULL,
    PersonalIncomeTax DECIMAL(12,1)  NOT NULL
)
''')


# Create Table for KPI Accounting
cursor.execute("""
    CREATE TABLE IF NOT EXISTS PerformanceEvaluationAccounting (
        PerformanceEvaluationAccountingId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        EmployeeId INT UNSIGNED NOT NULL,
        Month VARCHAR(20) NOT NULL,
        WorkPerformanceScore INT UNSIGNED NOT NULL,
        ConsciousnessScore INT UNSIGNED NOT NULL,
        AveragePaymentTime REAL NOT NULL,
        AverageDebtRecoveryTime REAL NOT NULL,
        CostPerTransaction DECIMAL(12,1)  NOT NULL,
        AverageProcessingTime REAL NOT NULL,
        PaymentErrorRate REAL NOT NULL,
        CostToRevenueRatio REAL NOT NULL,
        FOREIGN KEY (EmployeeId) REFERENCES Employee(EmployeeId)
    )
""")

# Tạo bảng KPI Accounting
cursor.execute('''
CREATE TABLE IF NOT EXISTS KPIAccounting (
    KPIAccountingId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    EmployeeId INT UNSIGNED NOT NULL,
    Month VARCHAR(20) NOT NULL,
    WorkPerformanceScore INT UNSIGNED NOT NULL,
    ConsciousnessScore INT UNSIGNED NOT NULL,
    AveragePaymentTime REAL NOT NULL,
    AverageDebtRecoveryTime REAL NOT NULL,
    CostPerTransaction DECIMAL(12,1) NOT NULL,
    AverageProcessingTime REAL NOT NULL,
    PaymentErrorRate REAL NOT NULL,
    CostToRevenueRatio REAL NOT NULL,
    FOREIGN KEY (EmployeeId) REFERENCES Employee(EmployeeId)
)
''')

db.commit()
db.close()