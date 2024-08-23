import pandas as pd

import mysql.connector

db = mysql.connector.connect(
    host='localhost', user='root', password='Thanhdua12@'
)

cursor = db.cursor()

cursor.execute("use DBCPN")
cursor.execute("ALTER DATABASE DBCPN CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")

# Create Table for Departments
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Department (
        DepartmentId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        DepartmentName VARCHAR(127) NOT NULL
    )
""")

# Create Table for Employees
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        EmployeeId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        FullName VARCHAR(127) NOT NULL,
        DateOfBirth DATE NOT NULL,
        Gender Enum('Male', 'Female') NOT NULL,
        Address VARCHAR(255) NOT NULL,
        PhoneNumber VARCHAR(15) NOT NULL,
        Email VARCHAR(127) NOT NULL,
        DepartmentId INT UNSIGNED NOT NULL,
        HireDate DATE NOT NULL,
        Salary DECIMAL(12,1)  NOT NULL,
        EmploymentStatus ENUM('Resigned', 'Employed', 'Probation', 'Submitted Resignation') NOT NULL,
        FOREIGN KEY (DepartmentId) REFERENCES Department(DepartmentId)
    )
""")

# Create Table for Applicants: ứng viên
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Applicant (
        ApplicantId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        FullName VARCHAR(127) NOT NULL,
        DateOfBirth DATE NOT NULL,
        Gender Enum('Male', 'Female') NOT NULL,
        Address VARCHAR(255) NOT NULL,
        PhoneNumber VARCHAR(15) NOT NULL UNIQUE,
        Email VARCHAR(127) NOT NULL UNIQUE,
        Level ENUM('intern', 'fresher', 'junior', 'senior') NOT NULL
    )
""")

# Create Table for Recruitment Channels: kênh tuyển dụng
cursor.execute("""
    CREATE TABLE IF NOT EXISTS RecruitmentChannel (
        RecruitmentChannelId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        ChannelName VARCHAR(127) NOT NULL,
        Cost DECIMAL(12,1)  NOT NULL,
        PostDate DATE NOT NULL
    )
""")

# Create Table for Job Positions: vị trí công việc
cursor.execute("""
    CREATE TABLE IF NOT EXISTS JobPosition (
        JobPositionId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        PositionName VARCHAR(127) NOT NULL,
        JobDescriptionLink VARCHAR(255) NOT NULL
    )
""")

# Create Table for Applications: ứng tuyển
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Application (
        ApplicationId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        ApplicationDate DATE NOT NULL,
        RecruitmentChannelId INT UNSIGNED NOT NULL,
        ApplicantId INT UNSIGNED NOT NULL,
        JobPositionId INT UNSIGNED NOT NULL,
        PassCV ENUM('Pass', 'Fail') NOT NULL,
        FOREIGN KEY (RecruitmentChannelId) REFERENCES RecruitmentChannel(RecruitmentChannelId),
        FOREIGN KEY (ApplicantId) REFERENCES Applicant(ApplicantId),
        FOREIGN KEY (JobPositionId) REFERENCES JobPosition(JobPositionId)
    )
""")

# Create Table for Interviews
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Interview (
        InterviewId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        ApplicantId INT UNSIGNED NOT NULL,
        InterviewDate DATE NOT NULL,
        InterviewResult ENUM('Cancel', 'Pass', 'Fail') NOT NULL,
        HireDate DATE,
        InterviewerId INT UNSIGNED,
        FOREIGN KEY (InterviewerId) REFERENCES Employee(EmployeeId),
        FOREIGN KEY (ApplicantId) REFERENCES Applicant(ApplicantId)
    )
""")

# Create Table for Performance Evaluations
cursor.execute("""
    CREATE TABLE IF NOT EXISTS PerformanceEvaluation (
        PerformanceEvaluationId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        EmployeeId INT UNSIGNED NOT NULL,
        EvaluationDate DATE NOT NULL,
        ConsciousnessScore INT NOT NULL,
        DisciplinaryViolations INT NOT NULL,
        UnexcusedAbsences INT NOT NULL,
        WorkPerformanceScore INT NOT NULL,
        OvertimeHours INT NOT NULL,
        FOREIGN KEY (EmployeeId) REFERENCES Employee(EmployeeId)
    )
""")

# Create Table for KPI HR
cursor.execute("""
    CREATE TABLE IF NOT EXISTS KPIHR (
        KPIHRId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        EmployeeId INT UNSIGNED NOT NULL,
        Date Date NOT NULL,
        RecruitmentApplications INT UNSIGNED  NOT NULL,
        PassRateFirstInterview DECIMAL(12,1) NOT NULL,
        CostPerHire DECIMAL(12,1)  NOT NULL,
        WorkPerformanceScore INT NOT NULL,
        ConsciousnessScore INT NOT NULL,
        FOREIGN KEY (EmployeeId) REFERENCES Employee(EmployeeId)
    )
""")

# Create Table for Error Codes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ErrorCode (
        ErrorCodeId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        ErrorDescription TEXT NOT NULL
    )
""")

# Create Table for Employee Errors
cursor.execute("""
    CREATE TABLE IF NOT EXISTS EmployeeError (
        EmployeeErrorId INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
        EmployeeId INT UNSIGNED NOT NULL,
        ErrorCodeId INT UNSIGNED NOT NULL,
        ErrorDate DATE NOT NULL,
        FOREIGN KEY (EmployeeId) REFERENCES Employee(EmployeeId),
        FOREIGN KEY (ErrorCodeId) REFERENCES ErrorCode(ErrorCodeId)
    )
""")


db.commit()
db.close()