from PySide6.QtCore import Qt, QPoint, QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QGuiApplication
from pet.pet import Pet
from desktop.pet_widget import PetWidget


class DesktopWindow(QWidget):

    def __init__(self):

        super().__init__()

        # Create UI
        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
        )
        

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.pet_widget = PetWidget()

        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.pet_widget)

        self.setLayout(layout)


        # Create Engines
        self.pet = Pet()

        # Connect Signals
        self.pet.frame_changed.connect(
            self.pet_widget.show_frame
        )

        self.pet.movement.position_changed.connect(
            self.update_position
        )
        
        # Load Assets
        self.pet.idle()

        self.resize(self.pet_widget.width(), self.pet_widget.height())
        
        # Position Window
        screen = QGuiApplication.primaryScreen()
        geometry = screen.availableGeometry()

        x = geometry.right() - self.width() - 20
        y = geometry.bottom() - self.height() - 20
        self.move(x, y)

        # Temporary Tests
        QTimer.singleShot(2000, self.test_walk)

    def update_position(self, point: QPoint):
        """Move the desktop window to the new position."""
        self.move(point)

    def test_walk(self):
        """Temporary method to test movement."""
        target = QPoint(100, self.y())
        self.pet.walk_to(self.pos(), target)

    