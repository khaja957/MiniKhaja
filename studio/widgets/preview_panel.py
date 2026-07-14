from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout


class PreviewPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Character Preview"))

        self.preview = QLabel("No Image")

        self.preview.setAlignment(Qt.AlignCenter)

        self.preview.setMinimumSize(500, 500)

        self.preview.setStyleSheet("""
            QLabel {
                border: 2px dashed gray;
                font-size: 20px;
            }
        """)

        layout.addWidget(self.preview)