from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
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
    
    def show_image(self, image_path):

        image_path = Path(image_path)

        if not image_path.exists():
            return

        pixmap = QPixmap(str(image_path))

        pixmap = pixmap.scaled(
                self.preview.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

        self.preview.setPixmap(pixmap)