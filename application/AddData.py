import pandas as pd
import mysql.connector




# HR 
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
        application_id = row["ApplicationId"]
        application_date = row["ApplicationDate"]
        recruitment_channel_id = row["RecruitmentChannelId"]
        job_position_id = row["JobPositionId"]
        pass_cv = row["PassCv"]


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
        
def add_to_Applicant(file_path):
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
                
                
def add_to_Interview(file_path):
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
        performance_evaluation_id = row["PerformanceEvaluationHRId"]
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
            (PerformanceEvaluationHRId, EmployeeId, EvaluationDate, ConsciousnessScore, DisciplinaryViolations, UnexcusedAbsences, WorkPerformanceScore, OvertimeHours)
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


# MKT                 
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
    # Kết nối tới cơ sở dữ liệu
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("USE DBCPN")  # Chọn cơ sở dữ liệu cần sử dụng
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Lặp qua từng hàng trong dữ liệu và chèn vào bảng KPIMKT
    for index, row in data.iterrows():
        kpi_mkt_id = row["KPIMKTId"]
        employee_id = row["EmployeeId"]
        date = row["Date"]
        work_performance_score = row["WorkPerformanceScore"]
        consciousness_score = row["ConsciousnessScore"]
        lead_count = row["LeadCount"]
        page_views = row["PageViews"]
        bounce_rate = row["BounceRate"]
        avg_time_on_page = row["AvgTimeOnPage"]
        likes = row["Likes"]
        comments = row["Comments"]
        shares = row["Shares"]
        keyword_ranking = row["KeywordRanking"]
        web_traffic = row["WebTraffic"]
        organic_keyword_count = row["OrganicKeywordCount"]
        conversion_count = row["ConversionCount"]
        exit_rate = row["ExitRate"]
        link_count = row["LinkCount"]

        cursor.execute(
            """
            INSERT INTO KPIMKT 
            (KPIMKTId, EmployeeId, Date, WorkPerformanceScore, ConsciousnessScore, LeadCount, PageViews, BounceRate, AvgTimeOnPage, Likes, Comments, Shares, KeywordRanking, WebTraffic, OrganicKeywordCount, ConversionCount, ExitRate, LinkCount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                EmployeeId = VALUES(EmployeeId),
                Date = VALUES(Date),
                WorkPerformanceScore = VALUES(WorkPerformanceScore),
                ConsciousnessScore = VALUES(ConsciousnessScore),
                LeadCount = VALUES(LeadCount),
                PageViews = VALUES(PageViews),
                BounceRate = VALUES(BounceRate),
                AvgTimeOnPage = VALUES(AvgTimeOnPage),
                Likes = VALUES(Likes),
                Comments = VALUES(Comments),
                Shares = VALUES(Shares),
                KeywordRanking = VALUES(KeywordRanking),
                WebTraffic = VALUES(WebTraffic),
                OrganicKeywordCount = VALUES(OrganicKeywordCount),
                ConversionCount = VALUES(ConversionCount),
                ExitRate = VALUES(ExitRate),
                LinkCount = VALUES(LinkCount)
            """,
            (kpi_mkt_id, employee_id, date, work_performance_score, consciousness_score, lead_count, page_views, bounce_rate, avg_time_on_page, likes, comments, shares, keyword_ranking, web_traffic, organic_keyword_count, conversion_count, exit_rate, link_count)
        )
    
    db.commit()  # Lưu thay đổi vào cơ sở dữ liệu
    db.close()
    
    
def add_to_Leads(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@"
    )
    cursor = db.cursor()
    cursor.execute("USE DBCPN")  # Chọn cơ sở dữ liệu cần sử dụng
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Duyệt qua từng hàng trong file Excel và chèn vào bảng Lead
    for index, row in data.iterrows():
        lead_id = row["LeadsId"]
        name = row["Name"]
        address = row["Address"]
        phone = row["Phone"]
        email = row["Email"]
        age = row["Age"]
        gender = row["Gender"]
        date = row["Date"]
        campaign_id = row["CampaignId"]
        status = row["Status"]
        score = row["Score"]
        
        cursor.execute("""
            INSERT INTO Leads (LeadsId, Name, Address, Phone, Email, Age, Gender, Date, CampaignId, Status, Score)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                Name = VALUES(Name),
                Address = VALUES(Address),
                Phone = VALUES(Phone),
                Email = VALUES(Email),
                Age = VALUES(Age),
                Gender = VALUES(Gender),
                Date = VALUES(Date),
                CampaignId = VALUES(CampaignId),
                Status = VALUES(Status),
                Score = VALUES(Score)
        """, (lead_id, name, address, phone, email, age, gender, date, campaign_id, status, score))
    
    # Xác nhận thay đổi và đóng kết nối
    db.commit()
    db.close()

                          
def add_to_PageView(file_path):
    # Kết nối tới cơ sở dữ liệu
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@"
    )
    cursor = db.cursor()
    cursor.execute("USE DBCPN")  # Chọn cơ sở dữ liệu cần sử dụng
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Duyệt qua từng hàng trong file Excel và chèn vào bảng PageView
    for index, row in data.iterrows():
        pageview_id = row["PageViewId"]
        date = row["Date"]
        page = row["Page"]
        page_views = row["PageViews"]
        bounce_rate = row["BounceRate"]
        avg_time_on_page = row["AvgTimeOnPage"]
        likes = row["Likes"]
        comments = row["Comments"]
        shares = row["Shares"]
        
        cursor.execute("""
            INSERT INTO PageView (PageViewId, Date, Page, PageViews, BounceRate, AvgTimeOnPage, Likes, Comments, Shares)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                Date = VALUES(Date),
                Page = VALUES(Page),
                PageViews = VALUES(PageViews),
                BounceRate = VALUES(BounceRate),
                AvgTimeOnPage = VALUES(AvgTimeOnPage),
                Likes = VALUES(Likes),
                Comments = VALUES(Comments),
                Shares = VALUES(Shares)
        """, (pageview_id, date, page, page_views, bounce_rate, avg_time_on_page, likes, comments, shares))
    
    # Xác nhận thay đổi và đóng kết nối
    db.commit()
    db.close()

                          
def add_to_PerformanceEvaluationMKT(file_path):
        # Kết nối tới cơ sở dữ liệu
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("USE DBCPN")  # Chọn cơ sở dữ liệu cần sử dụng
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    for index, row in data.iterrows():
        cursor.execute("""
            INSERT INTO PerformanceEvaluationMKT (PerformanceEvaluationMKTId, EmployeeId, Date, WorkPerformanceScore, ConsciousnessScore, LeadCount, PageViews, BounceRate, AvgTimeOnPage, Likes, Comments, Shares, KeywordRanking, WebTraffic, OrganicKeywordCount, ConversionCount, ExitRate, LinkCount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                EmployeeId = VALUES(EmployeeId),
                Date = VALUES(Date),
                WorkPerformanceScore = VALUES(WorkPerformanceScore),
                ConsciousnessScore = VALUES(ConsciousnessScore),
                LeadCount = VALUES(LeadCount),
                PageViews = VALUES(PageViews),
                BounceRate = VALUES(BounceRate),
                AvgTimeOnPage = VALUES(AvgTimeOnPage),
                Likes = VALUES(Likes),
                Comments = VALUES(Comments),
                Shares = VALUES(Shares),
                KeywordRanking = VALUES(KeywordRanking),
                WebTraffic = VALUES(WebTraffic),
                OrganicKeywordCount = VALUES(OrganicKeywordCount),
                ConversionCount = VALUES(ConversionCount),
                ExitRate = VALUES(ExitRate),
                LinkCount = VALUES(LinkCount)
        """, (
            row["PerformanceEvaluationMKTId"],
            row["EmployeeId"],
            row["Date"],
            row["WorkPerformanceScore"],
            row["ConsciousnessScore"],
            row["LeadCount"],
            row["PageViews"],
            row["BounceRate"],
            row["AvgTimeOnPage"],
            row["Likes"],
            row["Comments"],
            row["Shares"],
            row["KeywordRanking"],
            row["WebTraffic"],
            row["OrganicKeywordCount"],
            row["ConversionCount"],
            row["ExitRate"],
            row["LinkCount"]
        ))
    
    db.commit()
    db.close()
    
    
def add_to_SEO(file_path):
        # Kết nối tới cơ sở dữ liệu
    db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
    cursor = db.cursor()
    cursor.execute("USE DBCPN")  # Chọn cơ sở dữ liệu cần sử dụng
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    for index, row in data.iterrows():
        cursor.execute("""
            INSERT INTO SEO (SEOId, Creator, Platform, KeywordRanking, WebTraffic, OrganicKeywordCount, ConversionCount, ExitRate, LinkCount)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                Creator = VALUES(Creator),
                Platform = VALUES(Platform),
                KeywordRanking = VALUES(KeywordRanking),
                WebTraffic = VALUES(WebTraffic),
                OrganicKeywordCount = VALUES(OrganicKeywordCount),
                ConversionCount = VALUES(ConversionCount),
                ExitRate = VALUES(ExitRate),
                LinkCount = VALUES(LinkCount)
        """, (
            row["SEOId"],
            row["Creator"],
            row["Platform"],
            row["KeywordRanking"],
            row["WebTraffic"],
            row["OrganicKeywordCount"],
            row["ConversionCount"],
            row["ExitRate"],
            row["LinkCount"]
        ))
    
    db.commit()
    db.close()
    

# SALES 
def add_to_Products(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()

    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)

    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO Product (
        ProductId, ProductName, Description, UnitPrice, Remaining
    ) VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        ProductName = VALUES(ProductName),
        Description = VALUES(Description),
        UnitPrice = VALUES(UnitPrice),
        Remaining = VALUES(Remaining)
    """

    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['ProductId'], row['ProductName'], row['Description'], 
            row['UnitPrice'], row['Remaining']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
                
                
def add_to_Order(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()

    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)

    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO Orders (
        OrdersId, CustomerId, OrderDate, ProductId, TotalAmount
    ) VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        CustomerId = VALUES(CustomerId),
        OrderDate = VALUES(OrderDate),
        ProductId = VALUES(ProductId),
        TotalAmount = VALUES(TotalAmount)
    """

    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['OrdersId'], row['CustomerId'], row['OrderDate'],
            row['ProductId'], row['TotalAmount']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
                
                
def add_to_Payments(file_path):
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Thanhdua12@",
    database="DBCPN"
)
    cursor = db.cursor()
    data = pd.read_excel(file_path)
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO Payment (
        PaymentId, OrderId, PaymentDate, Amount
    ) VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        OrderId = VALUES(OrderId),
        PaymentDate = VALUES(PaymentDate),
        Amount = VALUES(Amount)
    """

    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['PaymentId'], row['OrderId'], row['PaymentDate'], 
            row['Amount']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
    

def add_to_KPISales(file_path):
# Kết nối tới cơ sở dữ liệu
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    data = pd.read_excel(file_path)
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO KPISale (
        KPISaleID, Employee, Date, WorkPerformanceScore, ConsciousnessScore, 
        CustomerCount, TotalRevenue, DealClosureRate
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        Employee = VALUES(Employee),
        Date = VALUES(Date),
        WorkPerformanceScore = VALUES(WorkPerformanceScore),
        ConsciousnessScore = VALUES(ConsciousnessScore),
        CustomerCount = VALUES(CustomerCount),
        TotalRevenue = VALUES(TotalRevenue),
        DealClosureRate = VALUES(DealClosureRate)
    """

    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['KPISaleID'], row['Employee'], row['Date'], 
            row['WorkPerformanceScore'], row['ConsciousnessScore'], 
            row['CustomerCount'], row['TotalRevenue'], 
            row['DealClosureRate']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()


def add_to_PerformanceEvaluationSales(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO PerformanceEvaluationSale (
        PerformanceEvaluationSaleId, Employee, Date, WorkPerformanceScore, ConsciousnessScore, CustomerCount, TotalRevenue, DealClosureRate
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        Employee = VALUES(Employee),
        Date = VALUES(Date),
        WorkPerformanceScore = VALUES(WorkPerformanceScore),
        ConsciousnessScore = VALUES(ConsciousnessScore),
        CustomerCount = VALUES(CustomerCount),
        TotalRevenue = VALUES(TotalRevenue),
        DealClosureRate = VALUES(DealClosureRate)
    """
    
    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['PerformanceEvaluationSaleId'], row['Employee'], row['Date'], 
            row['WorkPerformanceScore'], row['ConsciousnessScore'], row['CustomerCount'], 
            row['TotalRevenue'], row['DealClosureRate']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
    
     
# Accounting    
def add_to_ExpenseReports(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO ExpenseReport (
        ExpenseReportId, ReportDate, TotalAmount, EmployeeID, ReasonId, Status, AcceptDate
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        ReportDate = VALUES(ReportDate),
        TotalAmount = VALUES(TotalAmount),
        EmployeeID = VALUES(EmployeeID),
        ReasonId = VALUES(ReasonId),
        Status = VALUES(Status),
        AcceptDate = VALUES(AcceptDate)
    """
    
    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['ExpenseReportId'], row['ReportDate'], row['TotalAmount'], 
            row['EmployeeID'], row['ReasonId'], row['Status'], 
            row['AcceptDate']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
    
    
def add_to_Fund(file_path):
    # Kết nối tới cơ sở dữ liệu
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO Fund (
        FundId, Date, OperatingFund, ReserveFund, DevelopmentFund
    ) VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        Date = VALUES(Date),
        OperatingFund = VALUES(OperatingFund),
        ReserveFund = VALUES(ReserveFund),
        DevelopmentFund = VALUES(DevelopmentFund)
    """
    
    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['FundId'], row['Date'], row['OperatingFund'], 
            row['ReserveFund'], row['DevelopmentFund']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
    
    
def add_to_KPIAccounting(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO KPIAccounting (
        EmployeeId, Date, WorkPerformanceScore, ConsciousnessScore, AveragePaymentTime,
        AverageDebtRecoveryTime, CostPerTransaction, AverageProcessingTime, PaymentErrorRate,
        CostToRevenueRatio
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        Date = VALUES(Date),
        WorkPerformanceScore = VALUES(WorkPerformanceScore),
        ConsciousnessScore = VALUES(ConsciousnessScore),
        AveragePaymentTime = VALUES(AveragePaymentTime),
        AverageDebtRecoveryTime = VALUES(AverageDebtRecoveryTime),
        CostPerTransaction = VALUES(CostPerTransaction),
        AverageProcessingTime = VALUES(AverageProcessingTime),
        PaymentErrorRate = VALUES(PaymentErrorRate),
        CostToRevenueRatio = VALUES(CostToRevenueRatio)
    """
    
    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['EmployeeId'], row['Date'], row['WorkPerformanceScore'], 
            row['ConsciousnessScore'], row['AveragePaymentTime'], 
            row['AverageDebtRecoveryTime'], row['CostPerTransaction'], 
            row['AverageProcessingTime'], row['PaymentErrorRate'], 
            row['CostToRevenueRatio']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
    
                
def add_to_Payables(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO Payable (
        PayableId, Date, CustomerId, Amount, DueDate
    ) VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        Date = VALUES(Date),
        CustomerId = VALUES(CustomerId),
        Amount = VALUES(Amount),
        DueDate = VALUES(DueDate)
    """
    
    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['PayableId'], row['Date'], row['CustomerId'], 
            row['Amount'], row['DueDate']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
    
    
def add_to_PerformanceEvaluationAccounting(file_path):
    # Kết nối tới cơ sở dữ liệu
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO PerformanceEvaluationAccounting (
        EmployeeId, Date, WorkPerformanceScore, ConsciousnessScore, 
        AveragePaymentTime, AverageDebtRecoveryTime, CostPerTransaction, 
        AverageProcessingTime, PaymentErrorRate, CostToRevenueRatio
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        EmployeeId = VALUES(EmployeeId),
        Date = VALUES(Date),
        WorkPerformanceScore = VALUES(WorkPerformanceScore),
        ConsciousnessScore = VALUES(ConsciousnessScore),
        AveragePaymentTime = VALUES(AveragePaymentTime),
        AverageDebtRecoveryTime = VALUES(AverageDebtRecoveryTime),
        CostPerTransaction = VALUES(CostPerTransaction),
        AverageProcessingTime = VALUES(AverageProcessingTime),
        PaymentErrorRate = VALUES(PaymentErrorRate),
        CostToRevenueRatio = VALUES(CostToRevenueRatio)
    """
    
    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['EmployeeId'], row['Date'], row['WorkPerformanceScore'], 
            row['ConsciousnessScore'], row['AveragePaymentTime'], 
            row['AverageDebtRecoveryTime'], row['CostPerTransaction'],
            row['AverageProcessingTime'], row['PaymentErrorRate'],
            row['CostToRevenueRatio']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
    
    
def add_to_PersonalIncomeTax(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO PersonalIncomeTax (
        PersonalIncomeTaxId, TaxType
    ) VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE
        TaxType = VALUES(TaxType)
    """
    
    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            int(row['PersonalIncomeTaxId']), int(row['TaxType'])
        ))
    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
    
    
def add_to_Reason(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO Reason (
        ReasonId, Description
    ) VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE
        Description = VALUES(Description)
    """
    
    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['ReasonId'], row['Description']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
    
    
def add_to_Receivables(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO Receivable (
        ReceivableId, Date, CustomerId, Amount, DueDate
    ) VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        Date = VALUES(Date),
        CustomerId = VALUES(CustomerId),
        Amount = VALUES(Amount),
        DueDate = VALUES(DueDate)
    """
    
    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['ReceivableId'], row['Date'], row['CustomerId'],
            row['Amount'], row['DueDate']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
    
    
def add_to_Taxes(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO Tax (
        TaxId, Date, BusinessTax, IncomeTax, ValueAddedTax, PersonalIncomeTax
    ) VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        Date = VALUES(Date),
        BusinessTax = VALUES(BusinessTax),
        IncomeTax = VALUES(IncomeTax),
        ValueAddedTax = VALUES(ValueAddedTax),
        PersonalIncomeTax = VALUES(PersonalIncomeTax)
    """
    
    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['TaxId'], row['Date'], row['BusinessTax'], row['IncomeTax'], 
            row['ValueAddedTax'], row['PersonalIncomeTax']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()
    
    
def add_to_TaxTypeDescription(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO TaxTypeDescription (
        TaxTypeDescriptionId, Description, FixedTax, RateFixedTax
    ) VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        Description = VALUES(Description),
        FixedTax = VALUES(FixedTax),
        RateFixedTax = VALUES(RateFixedTax)
    """
    
    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['TaxTypeDescriptionId'], row['Description'], row['FixedTax'], row['RateFixedTax']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()


def add_to_Campaigns(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()

    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)

    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO Campaign (
        CampaignId, Marketer, Name, Brand, Target, StartDate, EndDate, 
        Description, Impression, Reach, Click, Share, Cmt, Inbox, Budget
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        Marketer = VALUES(Marketer),
        Name = VALUES(Name),
        Brand = VALUES(Brand),
        Target = VALUES(Target),
        StartDate = VALUES(StartDate),
        EndDate = VALUES(EndDate),
        Description = VALUES(Description),
        Impression = VALUES(Impression),
        Reach = VALUES(Reach),
        Click = VALUES(Click),
        Share = VALUES(Share),
        Cmt = VALUES(Cmt),
        Inbox = VALUES(Inbox),
        Budget = VALUES(Budget)
    """

    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['CampaignId'], row['Marketer'], row['Name'], row['Brand'], 
            row['Target'], row['StartDate'], row['EndDate'], row['Description'], 
            row['Impression'], row['Reach'], row['Click'], row['Share'], 
            row['Cmt'], row['Inbox'], row['Budget']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    db.close()
    
    
def add_to_Assets(file_path):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Thanhdua12@",
        database="DBCPN"
    )
    cursor = db.cursor()
    
    # Đọc dữ liệu từ file Excel
    data = pd.read_excel(file_path)
    
    # Chuẩn bị câu lệnh SQL để chèn dữ liệu
    sql = """
    INSERT INTO Asset (
        AssetId, ProductName, Quantity, UnitPrice
    ) VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        ProductName = VALUES(ProductName),
        Quantity = VALUES(Quantity),
        UnitPrice = VALUES(UnitPrice)
    """
    
    # Chèn dữ liệu vào cơ sở dữ liệu
    for index, row in data.iterrows():
        cursor.execute(sql, (
            row['AssetId'], row['ProductName'], row['Quantity'], row['UnitPrice']
        ))

    # Commit transaction và đóng kết nối
    db.commit()
    cursor.close()
    db.close()


def insert_data_from_excel(file_path, department, table):
    add_functions = {
        'HR': {
            'Application': add_to_Application,
            'Applicant': add_to_Applicant,
            'Department': add_to_Department,
            'Employee': add_to_Employee,
            'EmployeeError': add_to_EmployeeError,
            'ErrorCode': add_to_ErrorCode,
            'Interview': add_to_Interview,
            'JobPosition': add_to_JobPosition,
            'KPIHR': add_to_KPIHR,
            'PerformanceEvaluationHR': add_to_PerformanceEvaluationHR,
            'RecruitmentChannel': add_to_RecruitmentChannel
        },
        'MKT': {
            'Campaign': add_to_Campaigns,
            'KPIMKT': add_to_KPIMKT,
            'SEO': add_to_SEO,
            'Leads': add_to_Leads,
            'PageView': add_to_PageView,
            'PerformanceEvaluationMKT': add_to_PerformanceEvaluationMKT
        },
        'SALES': {
            'PerformanceEvaluationSale': add_to_PerformanceEvaluationSales,
            'KPISale': add_to_KPISales,
            'Orders': add_to_Order,
            'Product': add_to_Products,
            'Payment': add_to_Payments
        },
        'Accounting': {
            'Asset': add_to_Assets,
            'ExpenseReport': add_to_ExpenseReports,
            'Fund': add_to_Fund,
            'KPIAccounting': add_to_KPIAccounting,
            'Payable': add_to_Payables,
            'PerformanceEvaluationAccounting': add_to_PerformanceEvaluationAccounting,
            'PersonalIncomeTax': add_to_PersonalIncomeTax,
            'Reason': add_to_Reason,
            'Receivable': add_to_Receivables,
            'Tax': add_to_Taxes,
            'TaxTypeDescription': add_to_TaxTypeDescription
        }
    }

    file_path 
    department 
    table_name = table 

    # Gọi hàm tương ứng
    if department in add_functions and table_name in add_functions[department]:
        add_functions[department][table_name](file_path)
    else:
        print(f"No function found for department '{department}' and table '{table_name}'.")
