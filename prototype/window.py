from PySide6.QtWidgets import (
    QWidget,
    QGraphicsView,
    QGraphicsScene,
    QGraphicsPixmapItem,
    QVBoxLayout,
    QFrame,
)

from PySide6.QtCore import Qt


class CompanionWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.scene = QGraphicsScene(self)

        self.view = QGraphicsView(self.scene)

        self.view.setFrameShape(QFrame.NoFrame)

        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.view.setStyleSheet("""
            background: transparent;
            border: none;
        """)

        self.view.setAttribute(Qt.WA_TranslucentBackground)

        self.pixmap = QGraphicsPixmapItem()

        self.scene.addItem(self.pixmap)

        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.view)

        self.setLayout(layout)

    def fit_to_pixmap(self):

        rect = self.pixmap.boundingRect()

        self.scene.setSceneRect(rect)

        self.view.setSceneRect(rect)

        self.resize(int(rect.width()), int(rect.height()))