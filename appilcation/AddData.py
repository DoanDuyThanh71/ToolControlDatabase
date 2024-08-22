import pandas as pd
import pandas as pd

import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='Thanhdua12@'
)
cursor = db.cursor()
cursor.execute("use DBCPN")
cursor.execute("ALTER DATABASE DBCPN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")

# cursor.execute("SHOW TABLES")
# tables = cursor.fetchall()
# table_count = len(tables)
# print("Number of tables:", table_count)


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


def add_to_Department(file_path):
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("use DBCPN")
    
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
    
    db.commit()
    db.close()


def add_to_Application(file_path):
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("use DBCPN")  # Chọn cơ sở dữ liệu

    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)

    for index, row in data.iterrows():
        # Lấy dữ liệu từ file Excel
        applicant_id = row["ApplicantId"]
        full_name = row["FullName"]
        date_of_birth = row["DateOfBirth"]
        gender = row["Gender"]
        address = row["Address"]
        phone_number = row["PhoneNumber"]
        email = row["Email"]
        level = row["Level"]

        application_id = row["ApplicationId"]
        application_date = row["ApplicationDate"]
        recruitment_channel_id = row["RecruitmentChannelId"]
        job_position_id = row["JobPositionId"]
        pass_cv = row["PassCv"]

        # Chèn dữ liệu vào bảng Applicant
        cursor.execute(
            """
            INSERT INTO Applicant (ApplicantId, FullName, DateOfBirth, Gender, Address, PhoneNumber, Email, Level)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                FullName = VALUES(FullName),
                DateOfBirth = VALUES(DateOfBirth),
                Gender = VALUES(Gender),
                Address = VALUES(Address),
                PhoneNumber = VALUES(PhoneNumber),
                Email = VALUES(Email),
                Level = VALUES(Level)
            """,
            (applicant_id, full_name, date_of_birth, gender, address, phone_number, email, level)
        )

        # Chèn dữ liệu vào bảng Application
        cursor.execute(
            """
            INSERT INTO Application (ApplicationId, ApplicationDate, RecruitmentChannelId, ApplicantId, JobPositionId, PassCV)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                ApplicationDate = VALUES(ApplicationDate),
                RecruitmentChannelId = VALUES(RecruitmentChannelId),
                ApplicantId = VALUES(ApplicantId),
                JobPositionId = VALUES(JobPositionId),
                PassCV = VALUES(PassCV)
            """,
            (application_id, application_date, recruitment_channel_id, applicant_id, job_position_id, pass_cv)
        )
    
    # Xác nhận thay đổi
    db.commit()
    db.close()
        

def add_to_Employee(file_path):
    
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("use DBCPN")

    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    for index, row in data.iterrows():
        employee_id = row["EmployeeId"]  # Nếu có EmployeeId trong bảng
        full_name = row["FullName"]
        date_of_birth = row["DateOfBirth"]
        gender = row["Gender"]
        address = row["Address"]
        phone_number = row["PhoneNumber"]
        email = row["Email"]
        department_id = row["DepartmentId"]
        hire_date = row["HireDate"]
        salary = row["Salary"]
        employment_status = row["EmploymentStatus"]

        # Thực hiện câu lệnh INSERT hoặc UPDATE
        cursor.execute(
            """
    INSERT INTO Employee (EmployeeId, FullName, DateOfBirth, Gender, Address, PhoneNumber, Email, DepartmentId, HireDate, Salary, EmploymentStatus)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE 
        FullName = VALUES(FullName),
        DateOfBirth = VALUES(DateOfBirth),
        Gender = VALUES(Gender),
        Address = VALUES(Address),
        PhoneNumber = VALUES(PhoneNumber),
        Email = VALUES(Email),
        DepartmentId = VALUES(DepartmentId),
        HireDate = VALUES(HireDate),
        Salary = VALUES(Salary),
        EmploymentStatus = VALUES(EmploymentStatus)
""",
            (employee_id, full_name, date_of_birth, gender, address, phone_number, email, department_id, hire_date, salary, employment_status),
        )
    
    # Xác nhận thay đổi
    db.commit()
    db.close()
    
    
                
def add_to_EmployeeError(file_path):
 # Kết nối tới cơ sở dữ liệu
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("USE DBCPN")  # Chọn cơ sở dữ liệu cần sử dụng
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Lặp qua từng hàng trong dữ liệu và chèn vào bảng EmployeeError
    for index, row in data.iterrows():
        employee_error_id = row["EmployeeErrorId"]

        employee_id = row["EmployeeId"]
        error_code_id = row["ErrorCodeId"]
        error_date = row["ErrorDate"]
        
        cursor.execute(
            """
            INSERT INTO EmployeeError 
            (EmployeeErrorId, EmployeeId, ErrorCodeId, ErrorDate)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                EmployeeId = VALUES(EmployeeId),
                ErrorCodeId = VALUES(ErrorCodeId),
                ErrorDate = VALUES(ErrorDate)
            """,
            (employee_error_id, employee_id, error_code_id, error_date)
        )
    
    db.commit()  # Lưu thay đổi vào cơ sở dữ liệu
    db.close()  # Đóng kết nối cơ sở dữ liệu
                
                
def add_to_ErrorCode(file_path):
    # Kết nối tới cơ sở dữ liệu
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("USE DBCPN")  # Chọn cơ sở dữ liệu cần sử dụng
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Lặp qua từng hàng trong dữ liệu và chèn vào bảng ErrorCode
    for index, row in data.iterrows():
        error_code_id = row["ErrorCodeId"]
        error_description = row["ErrorDescription"]
        
        cursor.execute(
            """
            INSERT INTO ErrorCode 
            (ErrorCodeId, ErrorDescription)
            VALUES (%s, %s)
            ON DUPLICATE KEY UPDATE
                ErrorDescription = VALUES(ErrorDescription)
            """,
            (error_code_id, error_description)
        )
    
    db.commit()  # Lưu thay đổi vào cơ sở dữ liệu
    db.close()
                
                
def add_to_InterView(file_path):
    # Kết nối tới cơ sở dữ liệu
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("USE DBCPN")  # Chọn cơ sở dữ liệu cần sử dụng
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Lặp qua từng hàng trong dữ liệu và chèn vào bảng Interview
    for index, row in data.iterrows():
        interview_id = row["InterviewId"]
        applicant_id = row["ApplicantId"]
        interview_date = row["InterviewDate"]
        interview_result = row["InterviewResult"]
        hire_date = row["HireDate"]
        interviewer_id = row["InterviewerId"]
        
        cursor.execute(
            """
            INSERT INTO Interview 
            (InterviewId, ApplicantId, InterviewDate, InterviewResult, HireDate, InterviewerId)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                ApplicantId = VALUES(ApplicantId),
                InterviewDate = VALUES(InterviewDate),
                InterviewResult = VALUES(InterviewResult),
                HireDate = VALUES(HireDate),
                InterviewerId = VALUES(InterviewerId)
            """,
            (interview_id, applicant_id, interview_date, interview_result, hire_date, interviewer_id)
        )
    
    db.commit()  # Lưu thay đổi vào cơ sở dữ liệu
    db.close()  # Đóng kết nối cơ sở dữ liệu
                
                
def add_to_JobPosition(file_path):
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("use DBCPN")  # Chọn cơ sở dữ liệu

    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)

    for index, row in data.iterrows():
        # Lấy dữ liệu từ mỗi hàng trong file Excel
        job_position_id = row["JobPositionId"]
        position_name = row["PositionName"]
        job_description_link = row["JobDescriptionLink"]

        # Chèn dữ liệu vào bảng JobPosition
        cursor.execute(
            """
            INSERT INTO JobPosition (JobPositionId, PositionName, JobDescriptionLink)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                PositionName = VALUES(PositionName),
                JobDescriptionLink = VALUES(JobDescriptionLink)
            """,
            (job_position_id, position_name, job_description_link)
        )
    
    # Xác nhận thay đổi
    db.commit()
    db.close()
    
    
def add_to_KPIHR(file_path):
    # Kết nối tới cơ sở dữ liệu
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("USE DBCPN")  # Chọn cơ sở dữ liệu cần sử dụng
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Lặp qua từng hàng trong dữ liệu và chèn vào bảng KPIHR
    for index, row in data.iterrows():
        kpi_hr_id = row["KPIHRId"]
        employee_id = row["EmployeeId"]
        date = row["Date"]
        recruitment_applications = row["RecruitmentApplications"]
        pass_rate_first_interview = row["PassRateFirstInterview"]
        cost_per_hire = row["CostPerHire"]
        work_performance_score = row["WorkPerformanceScore"]
        consciousness_score = row["ConsciousnessScore"]
        
        cursor.execute(
            """
            INSERT INTO KPIHR 
            (KPIHRId, EmployeeId, Date, RecruitmentApplications, PassRateFirstInterview, CostPerHire, WorkPerformanceScore, ConsciousnessScore)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                EmployeeId = VALUES(EmployeeId),
                Date = VALUES(Date),
                RecruitmentApplications = VALUES(RecruitmentApplications),
                PassRateFirstInterview = VALUES(PassRateFirstInterview),
                CostPerHire = VALUES(CostPerHire),
                WorkPerformanceScore = VALUES(WorkPerformanceScore),
                ConsciousnessScore = VALUES(ConsciousnessScore)
            """,
            (kpi_hr_id, employee_id, date, recruitment_applications, pass_rate_first_interview, cost_per_hire, work_performance_score, consciousness_score)
        )
    
    db.commit()  # Lưu thay đổi vào cơ sở dữ liệu
    db.close()
    
    
                
def add_to_PerformanceEvaluationHR(file_path):
    # Kết nối tới cơ sở dữ liệu
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("USE DBCPN")  # Chọn cơ sở dữ liệu cần sử dụng
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Lặp qua từng hàng trong dữ liệu và chèn vào bảng PerformanceEvaluationHR
    for index, row in data.iterrows():
        performance_evaluation_id = row["PerformanceEvaluationId"]
        employee_id = row["EmployeeId"]
        evaluation_date = row["EvaluationDate"]
        consciousness_score = row["ConsciousnessScore"]
        disciplinary_violations = row["DisciplinaryViolations"]
        unexcused_absences = row["UnexcusedAbsences"]
        work_performance_score = row["WorkPerformanceScore"]
        overtime_hours = row["OvertimeHours"]
        
        cursor.execute(
            """
            INSERT INTO PerformanceEvaluationHR 
            (PerformanceEvaluationId, EmployeeId, EvaluationDate, ConsciousnessScore, DisciplinaryViolations, UnexcusedAbsences, WorkPerformanceScore, OvertimeHours)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                EmployeeId = VALUES(EmployeeId),
                EvaluationDate = VALUES(EvaluationDate),
                ConsciousnessScore = VALUES(ConsciousnessScore),
                DisciplinaryViolations = VALUES(DisciplinaryViolations),
                UnexcusedAbsences = VALUES(UnexcusedAbsences),
                WorkPerformanceScore = VALUES(WorkPerformanceScore),
                OvertimeHours = VALUES(OvertimeHours)
            """,
            (performance_evaluation_id, employee_id, evaluation_date, consciousness_score, disciplinary_violations, unexcused_absences, work_performance_score, overtime_hours)
        )
    
    # Lưu thay đổi và đóng kết nối
    db.commit()
    db.close()

                
def add_to_RecruitmentChannel(file_path):
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("use DBCPN")  # Chọn cơ sở dữ liệu

    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)

    for index, row in data.iterrows():
        # Lấy dữ liệu từ mỗi hàng trong file Excel
        recruitment_channel_id = row["RecruitmentChannelId"]
        channel_name = row["ChannelName"]
        cost = row["Cost"]
        post_date = row["PostDate"]

        # Chèn dữ liệu vào bảng RecruitmentChannel
        cursor.execute(
            """
            INSERT INTO RecruitmentChannel (RecruitmentChannelId, ChannelName, Cost, PostDate)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                ChannelName = VALUES(ChannelName),
                Cost = VALUES(Cost),
                PostDate = VALUES(PostDate)
            """,
            (recruitment_channel_id, channel_name, cost, post_date)
        )
    
    # Xác nhận thay đổi
    db.commit()
    db.close()


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
            add_to_PerformanceEvaluationHR(file_path)
        if table == 'RecruitmentChannel':
            add_to_RecruitmentChannel(file_path)
            
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
