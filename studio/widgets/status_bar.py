from PySide6.QtWidgets import QLabel


class StudioStatusBar(QLabel):

    def __init__(self):
        super().__init__()

        self.setText("Ready")
    
    def set_status(self, text: str):
        self.setText(text)        