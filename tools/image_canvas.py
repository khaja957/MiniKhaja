from PySide6.QtCore import QPoint, QRect, Qt
from PySide6.QtGui import QColor, QPainter, QPen, QPixmap
from PySide6.QtWidgets import QLabel


class ImageCanvas(QLabel):
    """Widget that displays an image and allows selecting a rectangle."""

    def __init__(self):
        super().__init__()
        self.selection_rect = QRect()

        self.pixmap_image = None

        self.start_point = QPoint()
        self.end_point = QPoint()

        self.selecting = False

    def set_image(self, pixmap: QPixmap):
        self.pixmap_image = pixmap
        self.setPixmap(pixmap)
        self.adjustSize()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.position().toPoint()
            self.end_point = self.start_point
            self.selecting = True
            self.update()

    def mouseMoveEvent(self, event):
        if self.selecting:
            self.end_point = event.position().toPoint()
            self.update()

    def mouseReleaseEvent(self, event):
        self.end_point = event.position().toPoint()

        self.selection_rect = QRect(
            self.start_point,
            self.end_point
        ).normalized()

        self.selecting = False

        self.update()

    def get_selection(self):
        return self.selection_rect

    def paintEvent(self, event):
        super().paintEvent(event)

        if self.start_point == self.end_point:
            return

        painter = QPainter(self)

        pen = QPen(QColor(0, 120, 255))
        pen.setWidth(2)

        painter.setPen(pen)

        painter.drawRect(QRect(self.start_point, self.end_point))