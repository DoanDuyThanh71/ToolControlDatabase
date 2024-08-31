from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QApplication
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QMovie

class ProgressDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Processing...")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout(self)

        # Hiển thị hình ảnh động
        self.loadingLabel = QLabel(self)
        self.loadingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loadingMovie = QMovie("loading.gif")
        self.loadingLabel.setMovie(self.loadingMovie)
        self.loadingMovie.start()
        layout.addWidget(self.loadingLabel)

        # Hiển thị dòng chữ "Loading..."
        self.loadingText = QLabel("Loading...", self)
        self.loadingText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.loadingText)

        self.cancelButton = QPushButton("Cancel", self)
        self.cancelButton.clicked.connect(self.cancel)
        layout.addWidget(self.cancelButton)

        self.progress = 0

    def set_progress(self, value):
        self.progress = value

    def cancel(self):
        self.close()
