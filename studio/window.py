from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
)

from studio.widgets.toolbar import Toolbar
from studio.widgets.prompt_panel import PromptPanel
from studio.widgets.preview_panel import PreviewPanel
from studio.widgets.status_bar import StudioStatusBar


class StudioWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mini Khaja Studio")

        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        self.toolbar = Toolbar()
        self.status = StudioStatusBar()

        content = QHBoxLayout()

        self.prompt_panel = PromptPanel()
        self.preview_panel = PreviewPanel()

        content.addWidget(self.prompt_panel, 1)
        content.addWidget(self.preview_panel, 2)

        main_layout.addWidget(self.toolbar)
        main_layout.addLayout(content)
        main_layout.addWidget(self.status)