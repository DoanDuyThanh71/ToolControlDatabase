from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class ErrorDialog(QDialog):  # Thay QWidget bằng QDialog
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Cảnh báo lỗi")
        self.resize(200, 50)
        layout = QVBoxLayout()

        self.label = QLabel(message)
        layout.addWidget(self.label)

        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.close)
        layout.addWidget(ok_button)

        self.setLayout(layout)

    def show_error(self, message):
        self.label.setText(message)
        self.exec()  # Sử dụng self.exec_() để hiển thị cửa sổ dialog modal
