from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit


class PromptPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Prompt Preview"))

        self.text = QTextEdit()

        self.text.setReadOnly(True)

        self.text.setPlainText(
            "Prompt will appear here..."
        )

        layout.addWidget(self.text)