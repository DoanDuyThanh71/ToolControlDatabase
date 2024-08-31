from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QDialogButtonBox

class CfDialog(QDialog):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Warning")
        self.resize(200, 50)
        layout = QVBoxLayout()

        self.label = QLabel(message)
        layout.addWidget(self.label)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def show_error(self, message):
        self.label.setText(message)
        return self.exec()  # Trả về mã kết quả của hộp thoại
