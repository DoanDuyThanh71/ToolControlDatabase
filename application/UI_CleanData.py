from tkinter import messagebox
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize
import pandas as pd 

from UI_Dialog import ErrorDialog
from UI_DialogCf import CfDialog
from UI_DialogNotification import NotificationDialog
from AddData import insert_data_from_excel
import os
import openpyxl as xlsx
import sys

class Worker(QtCore.QThread):
    
    finished = QtCore.pyqtSignal()
    def __init__(self, path, Department, Table):
        super().__init__()
        self.path = path
        self.Department = Department
        self.Table = Table

    def run(self):
        shell = False
        insert_data_from_excel(self.path, self.Department, self.Table)
            




class UI_clean(object):
    def __init__(self) -> None:
        self.path = None
        self.Department = None
        self.Table = None
        self.colSelection = None
        self.department_data = {
            "HR": ["Application", "Applicant" , "Department", "Employee", "EmployeeError", "ErrorCode", "Interview", "JobPosition", "KPIHR", "PerformanceEvaluationHR", "RecruitmentChannel"], 
            "MKT": ["Campaign", "SEO", "KPIMKT", "Leads", "PageView", "PerformanceEvaluationMKT"],
            "SALES": ["PerformanceEvaluationSale", "KPISale", "Orders", "Product", "Payment"],
            "Accounting": ["Asset", "ExpenseReport", "Fund", "KPIAccounting", "Payable", "PerformanceEvaluationAccounting", "PersonalIncomeTax", "Reason", "Receivable", "Tax", "TaxTypeDescription"]
        }

    def importData(self):
        self.colSelection = None
        self.labInfor.clear()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Import Data", "", "xlsx Files (*.xlsx)"
        )
        self.path = file_path
        data = []
        if file_path:
            file_name = os.path.basename(file_path)
            workbook = xlsx.load_workbook(file_path)
            sheet = workbook.active
            data = [list(row) for row in sheet.iter_rows(values_only=True)]

            if data:
                headers = data[0]
                num_rows = len(data) - 1
                row_out = min(num_rows, 100)
                num_cols = len(headers)
                self.data = data
                self.tabAns.setColumnCount(num_cols)
                self.tabAns.setRowCount(row_out)
                self.tabAns.setHorizontalHeaderLabels(map(str, headers))
                for row_idx, row_data in enumerate(data[1:100]):
                    for col_idx, cell_value in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(cell_value))
                        # Set font and background color for cells
                        item.setFont(QtGui.QFont("Arial", 10))
                        item.setBackground(QtGui.QColor(240, 240, 240))
                        self.tabAns.setItem(row_idx, col_idx, item)
                self.labInfor.setText(
                    f"Data imported successfully from file: \n{file_name}.\nRows: {num_rows}\n"
                )
                self.tabAns.resizeColumnsToContents()
            else:
                self.labInfor.setText("No file selected.")
            self.tabAns.resizeColumnsToContents()
            
    def check_data_exist(self, file_path, table_name, column_name):
        import mysql.connector
        import pandas as pd
        
        # Kết nối tới cơ sở dữ liệu
        db = mysql.connector.connect(host="localhost", user="root", password="Thanhdua12@")
        cursor = db.cursor()
        cursor.execute("USE DBCPN")  # Chọn cơ sở dữ liệu
        
        # Đọc dữ liệu từ file Excel
        data = pd.read_excel(file_path)
        
        # Lấy tất cả giá trị ID từ cơ sở dữ liệu
        query = f"SELECT {column_name} FROM {table_name}"
        cursor.execute(query)
        db_ids = set(row[0] for row in cursor.fetchall())
        
        if len(db_ids) == 0:
            return False
        
        # So sánh với các giá trị trong file Excel
        for index, row in data.iterrows():
            value = row[column_name]
            if value in db_ids:
                return True  # Nếu có giá trị không tồn tại trong cơ sở dữ liệu

        return False  # Nếu tất cả giá trị đều tồn tại

    def check_selection(self):
        try:
            selected_items = self.tabAns.selectedItems()
            
            if selected_items:
                selected_columns = set()
                for item in selected_items:
                    selected_columns.add(item.column())

                # print(f"Các cột đang được chọn: {list(selected_columns)}")
                self.colSelection = selected_columns
            else:
                # print("Không có cột nào được chọn.")
                pass
        except Exception as e:
            pass
        
        
    def print_data(self):
        if self.path is None:
            return
        path = self.path
        name = os.path.splitext(os.path.basename(path))[0]
        directory = os.path.dirname(path)
        new_file_name = os.path.join(directory, f"DataCheck_{name}.xlsx")
        
        try:
            df = pd.read_excel(new_file_name)
            
            num_cols = len(df.columns)
            num_rows = len(df) 
            columns = df.columns
            self.tabAns.clearContents()
            self.tabAns.setRowCount(num_rows)
            self.tabAns.setColumnCount(num_cols)

            self.tabAns.setHorizontalHeaderLabels(columns.tolist())
            self.tabAns.resizeColumnsToContents()

            for row_idx, row_data in df.iterrows():
                for col_idx, cell_value in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(cell_value))
                    self.tabAns.setItem(row_idx, col_idx, item)
            self.tabAns.resizeColumnsToContents()
            
        except Exception as e:
            return
            
            
    def edit_tab_ans(self, data):
        try:
            df = pd.DataFrame(data)
            # print(df)
            num_cols = len(df.columns)
            num_rows = len(df) 
            columns = df.columns
            self.tabAns.clearContents()
            self.tabAns.setRowCount(num_rows)
            self.tabAns.setColumnCount(num_cols)

            self.tabAns.setHorizontalHeaderLabels(columns.tolist())
            self.tabAns.resizeColumnsToContents()

            for row_idx, row_data in df.iterrows():
                for col_idx, cell_value in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(cell_value))
                    self.tabAns.setItem(row_idx, col_idx, item)
                    
            self.tabAns.resizeColumnsToContents()
            
        except Exception as e:
            return
        
    def run_app(self):   
        try:
            if not self.path:
                error_dialog = ErrorDialog("")
                error_dialog.show_error("No file selected. Please import a xlsx file.")
                return
                   
            if self.path:
                path = self.path
                name = os.path.splitext(os.path.basename(path))[0]
                directory = os.path.dirname(path)
                new_file_name = os.path.join(directory, f"DataCheck_{name}.xlsx")
                
                
                if os.path.exists(new_file_name):
                    
                    df = pd.read_excel(new_file_name)
                    action = self.actionClean.currentText()
                    
                    if action == "Export file":
                        try:
                            cf_dialog = CfDialog("Are you sure you want to replace and export the data?")
                            result = cf_dialog.show_error("Are you sure you want to replace and export the data?")
                            if result == ErrorDialog.DialogCode.Accepted:
                                df.to_excel(path, index=False)
                                os.remove(new_file_name)
                                ntf = NotificationDialog("")
                                ntf.show_ntf("Data exported successfully.")
                                return
                        except Exception as e:
                            ntf = NotificationDialog("")
                            ntf.show_ntf("Error while exporting data.")
                            return
                    
                    if action == "Restart file":
                        df = pd.read_excel(path) 
                        df.to_excel(new_file_name, index=False)
                        ntf = NotificationDialog("")
                        ntf.show_ntf("Data restart successfully.")
                        self.print_data()
                        return
                    
                    
                    if action == "Check Null":
                        if self.colSelection is None:
                            # Nếu không có cột nào được chọn, kiểm tra null toàn bộ bảng
                            null_count = df.isnull().sum().sum()
                        else:
                            # Nếu có cột được chọn, kiểm tra chỉ trong các cột được chọn
                            selected_columns = [df.columns[i] for i in self.colSelection if i < len(df.columns)]
                            
                            if len(selected_columns) == 0:
                                
                                # Nếu không có cột nào hợp lệ, thông báo lỗi
                                ntf = NotificationDialog("")
                                ntf.show_ntf("Invalid column selection.")
                                return
                            
                            null_df = df[df[selected_columns].isnull().any(axis=1)]  # Lấy các bản ghi có giá trị null trong các cột được chọn
                            null_count = len(null_df)
                        
                        if null_count > 0:
                            # self.edit_tab_ans(null_df)
                            ntf = NotificationDialog("")
                            cf_dialog = CfDialog(f"Found {null_count} null values. Are you sure you want to delete null data?")
                            result = cf_dialog.show_error(f"Found {null_count} null values. Are you sure you want to delete null data?")

                            if result == ErrorDialog.DialogCode.Accepted:
                                if self.colSelection is None:
                                    # Nếu không có cột được chọn, xóa null toàn bộ bảng
                                    df = df.dropna()
                                    self.print_data()
                                else:
                                    # Nếu có cột được chọn, xóa dòng chứa null trong cột được chọn
                                    df = df.dropna(subset=selected_columns)
                                    self.print_data()
                                
                                # Lưu kết quả sau khi xóa null
                                df.to_excel(new_file_name, index=False)
                                ntf.show_ntf("Data cleaned successfully.")
                        else:
                            # Thông báo nếu không có giá trị null
                            ntf = NotificationDialog("")
                            ntf.show_ntf("No null values found in the data.")
                        self.print_data()
                        return
                    
                    
                    
                    if action == "Check Non-numeric":
                        self.print_data()
                        if self.colSelection is None:
                            ntf = NotificationDialog("")
                            ntf.show_ntf("Please select at least one column to check.")
                            
                        else:
                            selected_columns = [df.columns[i] for i in self.colSelection if i < len(df.columns)]
                            if len(selected_columns) == 0:
                                ntf = NotificationDialog("")
                                ntf.show_ntf("Invalid column selection.")
                                return
                            
                            non_numeric_count = 0
                            for column in selected_columns:
                                try:
                                    df[column] = pd.to_numeric(df[column])
                                except:
                                    non_numeric_count += 1
                            
                            if non_numeric_count > 0:
                                cf_dialog = CfDialog(f"Found {non_numeric_count} non-numeric values. Are you sure you want to delete them data?")
                                result = cf_dialog.show_error(f"Found {non_numeric_count} non-numeric values. Are you sure you want to delete them data?")
                                
                                if result == ErrorDialog.DialogCode.Accepted:
                                    for column in selected_columns:
                                        # Sử dụng to_numeric với 'coerce', các giá trị không thể chuyển đổi sẽ thành NaN
                                        df[column] = pd.to_numeric(df[column], errors='coerce')

                                    # Xóa tất cả các dòng có chứa NaN (tức là các bản ghi không phải số)
                                    df = df.dropna(subset=selected_columns)
                                    df.to_excel(new_file_name, index=False)
                                    ntf = NotificationDialog("")
                                    ntf.show_ntf("Data delete successfully.")
                                    
                                    
                            else:
                                ntf = NotificationDialog("")
                                ntf.show_ntf("No non-numeric values found in the data.")
                            self.print_data()
                            return



                    if action == "Check Duplicate":
                        
                        self.print_data()
                        if self.colSelection is None:
                            ntf = NotificationDialog("")
                            ntf.show_ntf("Please select at least one column to check for duplicates.")
                            
                        else:
                            selected_columns = [df.columns[i] for i in self.colSelection if i < len(df.columns)]
                            
                            if len(selected_columns) == 0:
                                ntf = NotificationDialog("")
                                ntf.show_ntf("Invalid column selection.")
                                return
                            
                            # Kiểm tra các dòng trùng lặp dựa trên các cột đã chọn
                            duplicate_rows = df[df.duplicated(subset=selected_columns, keep=False)]
                            duplicate_count = len(duplicate_rows)
                            
                            if duplicate_count > 0:
                                # Thông báo và hỏi người dùng có muốn xóa các bản ghi trùng lặp không
                                cf_dialog = CfDialog(f"Found {duplicate_count} duplicate rows. Are you sure you want to delete them?")
                                result = cf_dialog.show_error(f"Found {duplicate_count} duplicate rows. Are you sure you want to delete them?")
                                
                                if result == ErrorDialog.DialogCode.Accepted:
                                    # Xóa các bản ghi trùng lặp
                                    df = df.drop_duplicates(subset=selected_columns, keep='first')
                                    df.to_excel(new_file_name, index=False)
                                    ntf = NotificationDialog("")
                                    ntf.show_ntf("Duplicate rows deleted successfully.")
                            else:
                                ntf = NotificationDialog("")
                                ntf.show_ntf("No duplicate rows found.")
                        
                        self.print_data()
                        return
 
                    
                    
                    if action == "Edit Data":
                        
                        try:
                            # Lấy số hàng và số cột trong tabAns
                            num_rows = self.tabAns.rowCount()
                            num_cols = self.tabAns.columnCount()

                            # Tạo một danh sách các danh sách để lưu toàn bộ dữ liệu từ tabAns
                            data = []
                            # Lặp qua các hàng và cột để lấy dữ liệu
                            for row_idx in range(num_rows):
                                row_data = []
                                for col_idx in range(num_cols):
                                    item = self.tabAns.item(row_idx, col_idx)
                                    # Nếu ô có giá trị, lấy text, nếu không thì để None
                                    row_data.append(item.text() if item else None)
                                data.append(row_data)

                            # Lấy tên cột từ tabAns
                            column_names = [self.tabAns.horizontalHeaderItem(col_idx).text() for col_idx in range(num_cols)]
                            
                            # Tạo DataFrame từ dữ liệu và tên cột
                            df = pd.DataFrame(data, columns=column_names)

                            # Lưu DataFrame vào file Excel
                            df.to_excel(new_file_name, index=False)
                            
                            # Hiển thị thông báo sau khi lưu thành công
                            ntf = NotificationDialog("")
                            ntf.show_ntf("Data saved successfully.")
                            
                        except Exception as e:
                            ntf = NotificationDialog("")
                            ntf.show_ntf("Error while saving data.")
                    
                    if action == "Check Data Exist":
                        try:    
                            if self.colSelection is None:
                                ntf = NotificationDialog("")
                                ntf.show_ntf("Please select at least one column to check.")
                                
                            else:
                                selected_columns = [df.columns[i] for i in self.colSelection if i < len(df.columns)]
                                if len(selected_columns) == 0:
                                    ntf = NotificationDialog("")
                                    ntf.show_ntf("Invalid column selection.")
                                    return
                                
                                for column in selected_columns:
                                    if self.check_data_exist(new_file_name, self.Table.currentText(), column):
                                        ntf = NotificationDialog("")
                                        ntf.show_ntf(f"Found data that already exists in the database.")
                                        return
                                
                                ntf = NotificationDialog("")
                                ntf.show_ntf("No data found that already exists in the database.")
                                return
                        except Exception as e:
                            ntf = NotificationDialog("")
                            ntf.show_ntf(f"Wrong Table Name")
                    
                    
                else:   
                    df = pd.read_excel(path) 
                    df.to_excel(new_file_name, index=False)  
                    
                    
                    
                                
        except Exception as e:
            print(e)
            return
            
            
    def go_back(self):
        from UI_Home import UI_Home
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_Home()
        self.ui.setupUi(self.window)
        self.window.show()
        QtCore.QTimer.singleShot(0, QtWidgets.QApplication.instance().activeWindow().close)


    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setFixedSize(1300, 616)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Button to import data
        self.btnImportData = QtWidgets.QPushButton(
            parent=self.centralwidget, clicked=lambda: self.importData()
        )
        self.btnImportData.setGeometry(QtCore.QRect(40, 40, 251, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnImportData.setFont(font)
        self.btnImportData.setObjectName("btnImportData")
        self.btnBack = QtWidgets.QPushButton(
            parent=self.centralwidget, clicked=lambda: self.go_back()
        )
        
        self.btnBack.setGeometry(QtCore.QRect(40, 10, 60, 20))
        font.setPointSize(12)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        
        icon = QtGui.QIcon("icon_back.png")
        self.btnBack.setIcon(icon)
        self.btnBack.clicked.connect(self.go_back)
        
        # Button to process
        self.btnProcess = QtWidgets.QPushButton(
                parent=self.centralwidget, clicked=lambda: self.run_app()
        )
        self.btnProcess.setGeometry(QtCore.QRect(950, 40, 301, 23))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btnProcess.setFont(font)
        self.btnProcess.setObjectName("btnProcess")

        # Label and Line Edit for Alpha
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
       
        self.Department = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Department.setGeometry(QtCore.QRect(160, 90, 131, 20))
        
        self.Department.setObjectName("Department")
        for department in self.department_data.keys():
            self.Department.addItem(department)

        self.Table = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Table.setGeometry(QtCore.QRect(160, 140, 131, 20))
        self.Department.setCurrentIndex(0)

        self.Department.currentIndexChanged.connect(self.update_table)
        


        # Label and Line Edit for Selected Row
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.Table = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Table.setGeometry(QtCore.QRect(160, 140, 131, 20))
        self.Table.setObjectName("Table")
        self.Table.addItem("")
        self.Table.addItem("")
        self.Table.addItem("")
        
        self.labe_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labe_3.setGeometry(QtCore.QRect(40, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.labe_3.setFont(font)
        self.labe_3.setObjectName("label_2")
        
        self.actionClean = QtWidgets.QComboBox(parent=self.centralwidget)
        self.actionClean.setGeometry(QtCore.QRect(160, 190, 131, 20))
        self.actionClean.setObjectName("actionClean")
        
        self.actionClean.addItem("Export file")
        self.actionClean.addItem("Restart file")
        self.actionClean.addItem("Edit Data")
        self.actionClean.addItem("Check Data Exist")
        self.actionClean.addItem("Check Null")
        self.actionClean.addItem("Check Duplicate")
        self.actionClean.addItem("Check Non-numeric")
        

        # Information Label
        self.labInfor = QtWidgets.QLabel(parent=self.centralwidget)
        self.labInfor.setGeometry(QtCore.QRect(950, 80, 350, 100))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.labInfor.setFont(font)
        self.labInfor.setText("")
        self.labInfor.setObjectName("labInfor")
        # Table Widget
        self.tabAns = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tabAns.setGeometry(QtCore.QRect(30, 240, 1230, 341))
        self.tabAns.setObjectName("tabAns")
        self.tabAns.setColumnCount(0)
        self.tabAns.setRowCount(0)

        # Setting up the main window
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.Department.currentIndexChanged.connect(self.update_table)
        self.tabAns.itemSelectionChanged.connect(self.check_selection)
        self.actionClean.currentIndexChanged.connect(self.print_data)

    def update_table(self):
            
            selected_department = self.Department.currentText()
            if selected_department == "":
                selected_department = self.Department.setCurrentIndex(0)
            tables = self.department_data.get(selected_department, [])

            self.Table.clear()
            for table in tables:
                self.Table.addItem(table)
     
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Clean Data"))
        self.btnImportData.setText(_translate("mainWindow", "Import Data"))
        self.btnProcess.setText(_translate("mainWindow", "Process"))
        self.label.setText(_translate("mainWindow", " Department"))
        self.label_2.setText(_translate("mainWindow", "Table"))
        self.labe_3.setText(_translate("mainWindow", "Action"))
        
        self.Department.setItemText(0, _translate("mainWindow", "HR"))
        self.Department.setItemText(1, _translate("mainWindow", "MKT"))
        self.Department.setItemText(2, _translate("mainWindow", "SALES"))
        self.Department.setItemText(3, _translate("mainWindow", "Accounting"))
        
        self.Table.clear()
        
        self.Table.addItem("Application")
        self.Table.addItem("Applicant")
        self.Table.addItem("Department")
        self.Table.addItem("Employee")
        self.Table.addItem("EmployeeError")
        self.Table.addItem("ErrorCode")
        self.Table.addItem("Interview")
        self.Table.addItem("JobPosition")
        self.Table.addItem("KPIHR")
        self.Table.addItem("PerformanceEvaluationHR")
        self.Table.addItem("RecruitmentChannel")
        
        # Phần retranslate cho actionClean
        self.actionClean.setItemText(0, _translate("mainWindow", "Export file"))
        self.actionClean.setItemText(1, _translate("mainWindow", "Restart file"))
        self.actionClean.setItemText(2, _translate("mainWindow", "Edit Data"))
        self.actionClean.setItemText(3, _translate("mainWindow", "Check Data Exist"))
        self.actionClean.setItemText(4, _translate("mainWindow", "Check Null"))
        self.actionClean.setItemText(5, _translate("mainWindow", "Check Non-numeric"))
        self.actionClean.setItemText(6, _translate("mainWindow", "Check Duplicate"))

        
        


if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = UI_clean()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())

