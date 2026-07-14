from PySide6.QtWidgets import QLabel


class StudioStatusBar(QLabel):

    def __init__(self):
        super().__init__()

        self.setText("Ready")