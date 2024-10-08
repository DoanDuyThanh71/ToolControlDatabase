from PyQt6 import QtCore, QtGui, QtWidgets
from UI_Dialog import ErrorDialog
from UI_DialogCf import CfDialog

# from AddData import insert_data_from_excel
import os
import openpyxl as xlsx
import sys

from UI_DialogNotification import NotificationDialog

class Worker(QtCore.QThread):
    
    finished = QtCore.pyqtSignal()
    def __init__(self, path, Department, Table):
        super().__init__()
        self.path = path
        self.Department = Department
        self.Table = Table
        

    def run(self):
        shell = False
        # insert_data_from_excel(self.path, self.Department, self.Table, )
        self.finished.emit()



class UI_DeleteData(object):
    def __init__(self) -> None:
        self.path = None
        self.Department = None
        self.Table = None
        # self.Id = None
        self.department_data = {
            "HR": ["Application", "Applicant" , "Department", "Employee", "EmployeeError", "ErrorCode", "Interview", "JobPosition", "KPIHR", "PerformanceEvaluationHR", "RecruitmentChannel"], 
            "MKT": ["Campaign", "SEO", "KPIMKT", "Leads", "PageView", "PerformanceEvaluationMKT"],
            "SALES": ["PerformanceEvaluationSale", "KPISale", "Orders", "Product", "Payment"],
            "Accounting": ["Asset", "ExpenseReport", "Fund", "KPIAccounting", "Payable", "PerformanceEvaluationAccounting", "PersonalIncomeTax", "Reason", "Receivable", "Tax", "TaxTypeDescription"]
        }

    def importData(self):
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
    
            
    def run_app(self):
        value = self.ID.text()
        if not self.path:
            if not value:
                error_dialog = ErrorDialog("No data delete")
                result = error_dialog.show_error("No data delete")
                return 
            cf_dialog = CfDialog("Are you sure you want to delete this data?")
            result = cf_dialog.show_error("Are you sure you want to delete this data?")

            if result == ErrorDialog.DialogCode.Accepted:
                self.delete_data()  
            else:
                ntf = NotificationDialog("")
                ntf.show_ntf("Data Deleted Cancel.")
            return
        else:
            cf_dialog = CfDialog("Are you sure you want to delete this data?")
            result = cf_dialog.show_error("Are you sure you want to delete this data?")
            if result == ErrorDialog.DialogCode.Accepted:
                self.delete_data() 
            else:
                ntf = NotificationDialog("")
                ntf.show_ntf("Deletion canceled.")
            return
                
 


    def on_process_finished(self):
        self.progress_dialog.close()


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
        
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        # Line Edit for ID
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.ID = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(160, 190, 131, 20))
        self.ID.setObjectName("ID")

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
        self.ID.textChanged.connect(self.print_data)
        self.Table.currentIndexChanged.connect(self.print_data)
        self.Department.currentIndexChanged.connect(self.print_data)
        

    def update_table(self):
            selected_department = self.Department.currentText()
            if selected_department == "":
                selected_department = self.Department.setCurrentIndex(0)
            tables = self.department_data.get(selected_department, [])

            self.Table.clear()
            for table in tables:
                self.Table.addItem(table)
    
    
    def delete_data(self):
        
        import mysql.connector
        import pandas as pd
        try:
            id_list = []
            id_value = self.ID.text()
            table_name = self.Table.currentText()
            
            # Kiểm tra xem đường dẫn file Excel có hợp lệ không
            if self.path:
                try:
                    # Đọc dữ liệu từ file Excel
                    data = pd.read_excel(self.path)
                    
                    if not data.empty:
                        # Lấy cột ID từ file Excel
                        id_column = data.columns[0]  # Giả sử cột ID là cột đầu tiên

                        # Tạo danh sách các ID từ file Excel
                        id_list = data[id_column].dropna().astype(int).tolist()
                    else:
                        ntf = NotificationDialog("")
                        ntf.show_ntf("The Excel file is empty or does not contain any valid data.")
                        
                except Exception as e:
                    ntf = NotificationDialog("")
                    ntf.show_ntf("Error reading Excel file.")
                    return
            
            if id_value:
                # Xử lý các ID nhập vào
                ranges = id_value.split(',')
                for item in ranges:
                    if '-' in item:
                        start, end = map(int, item.split('-'))
                        id_list.extend(range(start, end + 1))
                    else:
                        id_list.append(int(item.strip()))
            
            if id_list:
                try:
                    # Kết nối tới cơ sở dữ liệu MySQL
                    db = mysql.connector.connect(
                        host="localhost", 
                        user="root", 
                        password="Thanhdua12@", 
                        database="DBCPN"
                    )
                    cursor = db.cursor()            
                    total_deleted = 0
                    
                    # Thực hiện xoá các bản ghi với các ID trong danh sách
                    query = f"DELETE FROM {table_name} WHERE {table_name}Id = %s"
                    for id_value in id_list:
                        cursor.execute(query, (id_value,))
                        total_deleted += cursor.rowcount
                        
                    
                    # Xác nhận thay đổi
                    db.commit()
                    # Đóng kết nối
                    db.close()
                    
                    if total_deleted > 0:
                        ntf = NotificationDialog("")
                        ntf.show_ntf("Data Deleted successfully.")
                    else:
                        ntf = NotificationDialog("")
                        ntf.show_ntf("No matching records found to delete.")

                except Exception as e:
                    ntf = NotificationDialog("")
                    ntf.show_ntf("Error deleting data.")
                    # print(f"Error: {e}")
            
            else:
                ntf = NotificationDialog("")
                ntf.show_ntf("No valid IDs provided.")
                
            # Cập nhật giao diện người dùng
            self.tabAns.clearContents()
            self.tabAns.setRowCount(0)
            self.tabAns.setColumnCount(0)
            
        except Exception as e:
            ntf = NotificationDialog("")
            ntf.show_ntf("Error deleting data")

    
    
   

            
        
    def print_data(self):
        import mysql.connector
        
        id_value = self.ID.text()
        table_name = self.Table.currentText()
        
        if id_value:
            try:
                # Kết nối tới cơ sở dữ liệu MySQL
                db = mysql.connector.connect(
                    host="localhost", 
                    user="root", 
                    password="Thanhdua12@", 
                    database="DBCPN"  # Thay bằng tên cơ sở dữ liệu của bạn
                )
                cursor = db.cursor()

                # Lấy thông tin cột
                cursor.execute(f"SHOW COLUMNS FROM {table_name}")
                columns = [column[0] for column in cursor.fetchall()]
                
                id_list = []
                for part in id_value.split(','):
                    part = part.strip()
                    if '-' in part:
                        # Xử lý dãy ID có dấu gạch ngang
                        start, end = part.split('-')
                        id_list.extend(map(str, range(int(start), int(end) + 1)))
                    else:
                        id_list.append(part)
                        
                format_strings = ','.join(['%s'] * len(id_list))
                query = f"SELECT * FROM {table_name} WHERE {table_name}Id IN ({format_strings})"
                cursor.execute(query, tuple(id_list))

                # # Thực hiện truy vấn với tham số
                # query = f"SELECT * FROM {table_name} WHERE {table_name}Id = %s"
                # cursor.execute(query, (id_value,))

                # Lấy kết quả
                result = cursor.fetchall()

                # Đóng kết nối
                db.close()

                # Cập nhật QTableWidget
                num_cols = len(columns)
                num_rows = min(100,len(result))  
                

                self.tabAns.clearContents()
                self.tabAns.setRowCount(num_rows)
                self.tabAns.setColumnCount(num_cols)

                # Thêm tên cột vào dòng đầu tiên
                self.tabAns.setHorizontalHeaderLabels(columns)
                self.tabAns.resizeColumnsToContents()
                # for col_idx, column_name in enumerate(columns):
                #     item = QtWidgets.QTableWidgetItem(column_name)
                #     self.tabAns.setItem(0, col_idx, item)

                for row_idx, row_data in enumerate(result, start=0):
                    for col_idx, cell_value in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(cell_value))
                        self.tabAns.setItem(row_idx, col_idx, item)
                        
                self.tabAns.setStyleSheet("""
                QHeaderView::section {
                    border-bottom: 2px solid black;
                }
                QTableWidget::item {
                    border: none;
                }
            """)
                self.tabAns.resizeColumnsToContents()

            except Exception as e:
                print(f"Error: {e}")
        else:
            # Nếu ID rỗng, xóa dữ liệu hiện tại
            self.tabAns.clearContents()
            self.tabAns.setRowCount(0)
            self.tabAns.setColumnCount(0)

            
            
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Delete Data to Database"))
        self.btnImportData.setText(_translate("mainWindow", "Import Data"))
        self.btnProcess.setText(_translate("mainWindow", "Process"))
        self.label.setText(_translate("mainWindow", " Department"))
        self.label_2.setText(_translate("mainWindow", "Table"))
        self.label_3.setText(_translate("mainWindow", "ID"))
        
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
        self.Table.addItem("PerformanceEvaluation")
        self.Table.addItem("RecruitmentChannel")
        
        


if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = UI_DeleteData()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
