from PyQt6 import QtCore, QtGui, QtWidgets
from UI_Dialog import ErrorDialog
from UI_ProgressDialog import ProgressDialog
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
        self.finished.emit()



class UI_Add(object):
    def __init__(self) -> None:
        self.path = None
        self.Department = None
        self.Table = None
        
        self.department_data = {
            "HR": ["Application", "Department", "Employee", "EmployeeError", "ErrorCode", "InterView", "JobPosition", "KPIHR", "PerformanceEvaluation", "RecruitmentChannel"], 
            "MKT": ["Campaign", "KPIMKT", "Leads", "PageView", "PerformanceEvaluationMKT"],
            "SALES": ["PerformanceEvaluationSales", "KPISales", "Order", "Products"],
            "Accounting": ["Assets", "ExpenseReports", "Fund", "KPIAccounting", "Payables", "PerformanceEvaluationAccounting", "PersonalIncomeTax", "Reason", "Receivables", "Tax", "Taxes", "TaxTypeDescription"]
        }

    def importData(self):
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
                num_cols = len(headers)
                self.data = data
                self.tabAns.setColumnCount(num_cols)
                self.tabAns.setRowCount(9)
                self.tabAns.setHorizontalHeaderLabels(map(str, headers))
                for row_idx, row_data in enumerate(data[1:10]):
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
    def run_app(self):
        if not self.path:
            error_dialog = ErrorDialog("")
            error_dialog.show_error("No file selected. Please import a xlsx file.")
            return

                
        self.worker = Worker(self.path, self.Department.currentText(), self.Table.currentText())
        self.progress_dialog = ProgressDialog()
        self.progress_dialog.show()
        self.worker.finished.connect(self.on_process_finished)
        self.worker.start()
        

    def on_process_finished(self):
        self.progress_dialog.close()
        # self.tabAns.setRowCount(0)
        # file_name_with_ext = os.path.basename(self.path)
        # file_name, _ = os.path.splitext(file_name_with_ext)
        # output_file_name = file_name + "_output.txt"
        # with open(output_file_name, "r") as file:
        #     reader = xlsx.reader(file, delimiter="\t")
        #     column_names = next(reader)
        #     self.tabAns.setColumnCount(len(column_names))
        #     self.tabAns.setHorizontalHeaderLabels(column_names)

        #     for row_idx, row in enumerate(reader):
        #         self.tabAns.insertRow(row_idx)
        #         for col_idx, cell_value in enumerate(row):
        #             item = QtWidgets.QTableWidgetItem(str(cell_value))
        #             item.setFont(QtGui.QFont("Arial", 10))
        #             item.setBackground(QtGui.QColor(240, 240, 240))
        #             self.tabAns.setItem(row_idx, col_idx, item)

        # num_columns = self.tabAns.columnCount()

        # # Loop through all columns and set bold font for headers
        # for col_idx in range(min(num_columns, 7)):  # Only for the first 7 columns
        #     header_item = self.tabAns.horizontalHeaderItem(col_idx)
        #     if header_item is not None:
        #         font = QtGui.QFont()
        #         font.setBold(True)
        #         header_item.setFont(font)

        # self.tabAns.setWordWrap(True)

        # # Set the width for the first 7 columns
        # first_column_width = round(0.4 * self.tabAns.width())
        # self.tabAns.setColumnWidth(0, first_column_width)
        # self.tabAns.setColumnWidth(1, round(0.1 * self.tabAns.width()))
        # self.tabAns.setColumnWidth(2, round(0.15 * self.tabAns.width()))
        # self.tabAns.setColumnWidth(3, round(0.15 * self.tabAns.width()))
        # self.tabAns.setColumnWidth(4, round(0.0932 * self.tabAns.width()))
        # self.tabAns.setColumnWidth(5, round(0.0932 * self.tabAns.width()))

        # # Hide the remaining columns
        # for col_idx in range(6, num_columns):
        #     self.tabAns.setColumnHidden(col_idx, True)

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
        mainWindow.setWindowTitle(_translate("mainWindow", "Add Data to Database"))
        self.btnImportData.setText(_translate("mainWindow", "Import Data"))
        self.btnProcess.setText(_translate("mainWindow", "Process"))
        self.label.setText(_translate("mainWindow", " Department"))
        self.label_2.setText(_translate("mainWindow", "Table"))
        
        self.Department.setItemText(0, _translate("mainWindow", "HR"))
        self.Department.setItemText(1, _translate("mainWindow", "MKT"))
        self.Department.setItemText(2, _translate("mainWindow", "SALES"))
        self.Department.setItemText(3, _translate("mainWindow", "Accounting"))
        
        self.Table.clear()
        self.Table.addItem("Application")
        self.Table.addItem("Department")
        self.Table.addItem("Employee")
        self.Table.addItem("EmployeeError")
        self.Table.addItem("ErrorCode")
        self.Table.addItem("InterView")
        self.Table.addItem("JobPosition")
        self.Table.addItem("KPIHR")
        self.Table.addItem("PerformanceEvaluation")
        self.Table.addItem("RecruitmentChannel")
        
        


if __name__ == "__main__":
    import sys


    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = UI_Add()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())