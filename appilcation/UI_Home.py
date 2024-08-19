from PyQt6 import QtCore, QtGui, QtWidgets
from UI_AddingData import UI_Add
from PyQt6 import QtCore, QtGui, QtWidgets


class UI_Home(object):
    def openReducedData(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_Add()
        self.ui.setupUi(self.window)
        self.window.show()
        QtCore.QTimer.singleShot(
            0, QtWidgets.QApplication.instance().activeWindow().close
        )

    # def openReinforcement(self):
    #     self.window = QtWidgets.QMainWindow()
    #     # self.ui = Ui_Reinforcement()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    #     QtCore.QTimer.singleShot(
    #         0, QtWidgets.QApplication.instance().activeWindow().close
    #     )

    # def openIFPD(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = UI_IFPD()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    #     QtCore.QTimer.singleShot(
    #         0, QtWidgets.QApplication.instance().activeWindow().close
    #     )

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
        self.addData.clicked.connect(self.openReducedData)
        self.addData.installEventFilter(self.addData)

        self.btnReinforcement = QtWidgets.QPushButton(self.centralwidget)
        self.btnReinforcement.setGeometry(QtCore.QRect(90, 230, 630, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnReinforcement.setFont(font)
        self.btnReinforcement.setObjectName("btnReinforcement")
        # self.btnReinforcement.clicked.connect(self.openReinforcement)
        self.btnReinforcement.installEventFilter(self.addData)

        self.btnIFPD = QtWidgets.QPushButton(self.centralwidget)
        self.btnIFPD.setGeometry(QtCore.QRect(90, 330, 630, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnIFPD.setFont(font)
        self.btnIFPD.setObjectName("btnIFPD")
        # self.btnIFPD.clicked.connect(self.openIFPD)
        self.btnIFPD.installEventFilter(self.addData)

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
        if obj == self.addData or obj == self.btnReinforcement or obj == self.btnIFPD:
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
        self.btnReinforcement.setText(
            _translate(
                "MainWindow",
                "Incremental attribute reduction algorithm on the decision when adding object set",
            )
        )
        self.btnIFPD.setText(
            _translate(
                "MainWindow",
                "Incremental attribute reduction algorithm on the decision when removing object set",
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

