import mysql.connector

db = mysql.connector.connect(
    host = 'localhost', user = 'root', password = 'Thanhdua12@'
)

cursor = db.cursor()


cursor.execute("use HR")
cursor.execute("ALTER DATABASE HR CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")

# Create Table for Departments
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Department (
        Id INT PRIMARY KEY AUTO_INCREMENT,
        DepartmentName VARCHAR(100) NOT NULL
    )
""")

# Create Table for Employees
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        Id INT PRIMARY KEY AUTO_INCREMENT,
        FullName VARCHAR(100) NOT NULL,
        DateOfBirth DATE NOT NULL,
        Gender VARCHAR(10) NOT NULL,
        Address VARCHAR(255) NOT NULL,
        PhoneNumber VARCHAR(15) NOT NULL,
        Email VARCHAR(100) NOT NULL,
        DepartmentId INT NOT NULL,
        HireDate DATE NOT NULL,
        EmploymentStatus ENUM('Resigned', 'Employed', 'Probation', 'Submitted Resignation') NOT NULL,
        FOREIGN KEY (DepartmentId) REFERENCES Department(Id)
    )
""")


# Create Table for Applicants
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Applicant (
        Id INT PRIMARY KEY AUTO_INCREMENT,
        FullName VARCHAR(100) NOT NULL,
        DateOfBirth DATE NOT NULL,
        Gender VARCHAR(10) NOT NULL,
        Address VARCHAR(255) NOT NULL,
        PhoneNumber VARCHAR(15) NOT NULL UNIQUE,
        Email VARCHAR(100) NOT NULL UNIQUE,
        Level ENUM('intern', 'fresher', 'junior', 'senior') NOT NULL
    )
""")

# Create Table for Recruitment Channels
cursor.execute("""
    CREATE TABLE IF NOT EXISTS RecruitmentChannel (
        Id INT PRIMARY KEY AUTO_INCREMENT,
        ChannelName VARCHAR(100) NOT NULL,
        Cost DECIMAL(10, 2) NOT NULL,
        PostDate DATE NOT NULL
    )
""")

# Create Table for Job Positions
cursor.execute("""
    CREATE TABLE IF NOT EXISTS JobPosition (
        Id INT PRIMARY KEY AUTO_INCREMENT,
        PositionName VARCHAR(100) NOT NULL,
        JobDescriptionLink VARCHAR(255) NOT NULL
    )
""")

# Create Table for Applications
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Application (
        Id INT PRIMARY KEY AUTO_INCREMENT,
        ApplicationDate DATE NOT NULL,
        RecruitmentChannelId INT NOT NULL,
        ApplicantId INT NOT NULL,
        JobPositionId INT NOT NULL,
        PassCV ENUM('Pass', 'Fail') NOT NULL,
        FOREIGN KEY (RecruitmentChannelId) REFERENCES RecruitmentChannel(Id),
        FOREIGN KEY (ApplicantId) REFERENCES Applicant(Id),
        FOREIGN KEY (JobPositionId) REFERENCES JobPosition(Id)
    )
""")

# Create Table for Interviews
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Interview (
        Id INT PRIMARY KEY AUTO_INCREMENT,
        ApplicantId INT NOT NULL,
        InterviewDate DATE NOT NULL,
        InterviewResult ENUM('Cancel', 'Pass', 'Fail') NOT NULL,
        HireDate DATE,
        InterviewerId INT,
        FOREIGN KEY (InterviewerId) REFERENCES Employee(Id),
        FOREIGN KEY (ApplicantId) REFERENCES Applicant(Id)
    )
""")


# Create Table for Performance Evaluations
cursor.execute("""
    CREATE TABLE IF NOT EXISTS PerformanceEvaluation (
        Id INT PRIMARY KEY AUTO_INCREMENT,
        EmployeeId INT NOT NULL,
        EvaluationDate DATE NOT NULL,
        ConsciousnessScore INT NOT NULL,
        DisciplinaryViolations INT NOT NULL,
        UnexcusedAbsences INT NOT NULL,
        WorkPerformanceScore INT NOT NULL,
        OvertimeHours INT NOT NULL,
        FOREIGN KEY (EmployeeId) REFERENCES Employee(Id)
    )
""")

# Create Table for KPI
cursor.execute("""
    CREATE TABLE IF NOT EXISTS KPIHRM (
        Id INT PRIMARY KEY AUTO_INCREMENT,
        Month VARCHAR(20) NOT NULL,
        DepartmentId INT NOT NULL,
        RecruitmentApplications INT NOT NULL,
        PassRateFirstInterview DECIMAL(5, 2) NOT NULL,
        CostPerHire DECIMAL(10, 2) NOT NULL,
        TrainingSessions INT NOT NULL,
        TrainingSatisfaction DECIMAL(5, 2) NOT NULL,
        AdminProcessSatisfaction DECIMAL(5, 2) NOT NULL,
        FOREIGN KEY (DepartmentId) REFERENCES Department(Id)
    )
""")

# Create Table for Error Codes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ErrorCode (
        Id INT PRIMARY KEY AUTO_INCREMENT,
        ErrorCode VARCHAR(10) NOT NULL,
        ErrorDescription VARCHAR(255) NOT NULL
    )
""")

# Create Table for Employee Errors
cursor.execute("""
    CREATE TABLE IF NOT EXISTS EmployeeError (
        Id INT PRIMARY KEY AUTO_INCREMENT,
        EmployeeId INT NOT NULL,
        ErrorCodeId INT NOT NULL,
        ErrorDate DATE NOT NULL,
        FOREIGN KEY (EmployeeId) REFERENCES Employee(Id),
        FOREIGN KEY (ErrorCodeId) REFERENCES ErrorCode(Id)
    )
""")

db.commit()
