from PyQt6 import QtCore, QtGui, QtWidgets
from UI_AddingData import UI_Add
from UI_UpdateData import UI_Update
from UI_DeleteData import UI_DeleteData
from PyQt6 import QtCore, QtGui, QtWidgets


class UI_Home(object):
    def openAddData(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_Add()
        self.ui.setupUi(self.window)
        self.window.show()
        QtCore.QTimer.singleShot(
            0, QtWidgets.QApplication.instance().activeWindow().close
        )

    def openUpDateData(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_Update()
        self.ui.setupUi(self.window)
        self.window.show()
        QtCore.QTimer.singleShot(
            0, QtWidgets.QApplication.instance().activeWindow().close
        )

    def OpenDeleteData(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_DeleteData()
        self.ui.setupUi(self.window)
        self.window.show()
        QtCore.QTimer.singleShot(
            0, QtWidgets.QApplication.instance().activeWindow().close
        )

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 477)
        MainWindow.setFixedSize(800, 477)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 751, 40))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")

        self.addData = QtWidgets.QPushButton(self.centralwidget)
        self.addData.setGeometry(QtCore.QRect(90, 130, 630, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addData.setFont(font)
        self.addData.setObjectName("addData")
        self.addData.clicked.connect(self.openAddData)
        self.addData.installEventFilter(self.addData)

        self.updateData = QtWidgets.QPushButton(self.centralwidget)
        self.updateData.setGeometry(QtCore.QRect(90, 230, 630, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.updateData.setFont(font)
        self.updateData.setObjectName("updateData")
        self.updateData.clicked.connect(self.openUpDateData)
        self.updateData.installEventFilter(self.addData)

        self.deleteData = QtWidgets.QPushButton(self.centralwidget)
        self.deleteData.setGeometry(QtCore.QRect(90, 330, 630, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.deleteData.setFont(font)
        self.deleteData.setObjectName("deleteData")
        self.deleteData.clicked.connect(self.OpenDeleteData)
        self.deleteData.installEventFilter(self.addData)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def eventFilter(self, obj, event):
        if obj == self.addData or obj == self.updateData or obj == self.deleteData:
            if event.type() == QtCore.QEvent.Type.Enter:
                self.animateButton(obj, True)
            elif event.type() == QtCore.QEvent.Type.Leave:
                self.animateButton(obj, False)
        return super().eventFilter(obj, event)

    def animateButton(self, button, hovered):
        anim = QtCore.QPropertyAnimation(button, b'size')
        if hovered:
            anim.setEndValue(QtCore.QSize(650, 51))
        else:
            anim.setEndValue(QtCore.QSize(630, 41))
        anim.setDuration(100)
        anim.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(
            _translate(
                "MainWindow",
                "Tool Control Database",
            )
        )
        self.addData.setText(
            _translate(
                "MainWindow",
                "Add data to database",
            )
        )
        self.updateData.setText(
            _translate(
                "MainWindow",
                "Update data to database",
            )
        )
        self.deleteData.setText(
            _translate(
                "MainWindow",
                "Delete data from database",
            )
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_Home()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

