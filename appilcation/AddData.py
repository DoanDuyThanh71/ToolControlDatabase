import pandas as pd
import pandas as pd

import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='Thanhdua12@'
)

cursor = db.cursor()

cursor.execute("use DBCPN")
cursor.execute("ALTER DATABASE DBCPN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
table_count = len(tables)
# print("Number of tables:", table_count)

cursor.execute("SELECT * FROM Department")

# for table in tables:
#     print(table[0])

# cursor.execute("DESCRIBE Department")
# columns = cursor.fetchall()
# for column in columns:
#     print(column[0])
# Delete a value from the table


# cursor.execute("""
#         DELETE FROM employee
#         WHERE DepartmentId IN (SELECT DepartmentId FROM department)
#     """)

# cursor.execute("DELETE FROM Department")
# db.commit()

def check_data(file_path, table_name):
    data = pd.read_excel(file_path)
    # Check for null values
    if data.isnull().values.any():
        print("There are null values in the data.")
    else:
        print("There are no null values in the data.")
    
    # Check for duplicate values
    if data.duplicated().values.any():
        print("There are duplicate values in the data.")
    else:
        print("There are no duplicate values in the data.")
    
    # Check for data types
    print(data.dtypes)
    

def add_to_Department(file_path):
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("use DBCPN")

    # cursor.execute("SELECT * FROM Department")

    data = pd.read_excel(file_path)
    for index, row in data.iterrows():
        department_id = row["DepartmentId"]
        department_name = row["DepartmentName"]
        cursor.execute(
            """
    INSERT INTO Department (DepartmentID, DepartmentName)
    VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE DepartmentName = VALUES(DepartmentName)
""",
            (department_id, department_name),
        )
    
    cursor.execute("SELECT * FROM Department")
    result = cursor.fetchall()
    for row in result:
        print(row)
            
    
    db.commit()
    db.close()


def add_to_Application(file_path):
    1        

def add_to_Employee(file_path):
                1
def add_to_EmployeeError(file_path):
                1
def add_to_ErrorCode(file_path):
                1
def add_to_InterView(file_path):
                1
def add_to_JobPosition(file_path):
                1
def add_to_KPIHR(file_path):
                1
def add_to_PerformanceEvaluation(file_path):
                1
def add_to_RecruitmentChannel(file_path):
                1

def add_to_KPIMKT(file_path):
                1
def add_to_Leads(file_path):
                1
def add_to_PageView(file_path):
                1
def add_to_PerformanceEvaluationMKT(file_path):
                1

def add_to_KPISales(file_path):
                1
def add_to_Order(file_path):
                1
def add_to_Products(file_path):
                1

def add_to_ExpenseReports(file_path):
                1
def add_to_Fund(file_path):
                1
def add_to_KPIAccounting(file_path):
                1
def add_to_Payables(file_path):
                1
def add_to_PerformanceEvaluationAccounting(file_path):
                1
def add_to_PersonalIncomeTax(file_path):
                1
def add_to_Reason(file_path):
                1
def add_to_Receivables(file_path):
                1
def add_to_Tax(file_path):
                1
def add_to_Taxes(file_path):
                1
def add_to_TaxTypeDescription(file_path):
                1

def add_to_Campaign(file_path):
    1
def add_to_Assets(file_path):
    2

def add_to_PerformanceEvaluationSales(file_path):
    1


def insert_data_from_excel(file_path, department, table):
    if department == 'HR':
        if table == 'Application':
            add_to_Application(file_path)
        if table == 'Department':
            add_to_Department(file_path)
        if table == 'Employee':
            add_to_Employee(file_path)
        if table == 'EmployeeError':
            add_to_EmployeeError(file_path)
        if table == 'ErrorCode':
            add_to_ErrorCode(file_path)
        if table == 'InterView':    
            add_to_InterView(file_path)
        if table == 'JobPosition':
            add_to_JobPosition(file_path)
        if table == 'KPIHR':
            add_to_KPIHR(file_path)
        if table == 'PerformanceEvaluation':
            add_to_PerformanceEvaluation(file_path)
        if table == 'RecruitmentChannel':
            add_to_RecruitmentChannel(file_path)
            # ["Campaign", "KPIMKT", "Leads", "PageView", "PerformanceEvaluationMKT"]:
    elif department == 'MKT':
        if table == 'Campaign':
            add_to_Campaign(file_path)
        if table == 'KPIMKT':
            add_to_KPIMKT(file_path)
        if table == 'Leads':
            add_to_Leads(file_path)
        if table == 'PageView':
            add_to_PageView(file_path)
        if table == 'PerformanceEvaluationMKT':
            add_to_PerformanceEvaluationMKT(file_path)
        
    elif department == 'SALES':
        if table == 'PerformanceEvaluationSales':
            add_to_PerformanceEvaluationSales(file_path)
        if table == 'KPISales':
            add_to_KPISales(file_path)
        if table == 'Order':
            add_to_Order(file_path)
        if table == 'Products':
            add_to_Products(file_path)
    
    elif department == 'Accounting':
        if table == 'Assets':
            add_to_Assets(file_path)
        if table == 'ExpenseReports':
            add_to_ExpenseReports(file_path)
        if table == 'Fund':
            add_to_Fund(file_path)
        if table == 'KPIAccounting':
            add_to_KPIAccounting(file_path)
        if table == 'Payables':
            add_to_Payables(file_path)
        if table == 'PerformanceEvaluationAccounting':
            add_to_PerformanceEvaluationAccounting(file_path)
        if table == 'PersonalIncomeTax':
            add_to_PersonalIncomeTax(file_path)
        if table == 'Reason':
            add_to_Reason(file_path)
        if table == 'Receivables':
            add_to_Receivables(file_path)
        if table == 'Tax':
            add_to_Tax(file_path)
        if table == 'Taxes':
            add_to_Taxes(file_path)
        if table == 'TaxTypeDescription':
            add_to_TaxTypeDescription(file_path)
