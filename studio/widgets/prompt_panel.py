from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit


class PromptPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Prompt Preview"))

        self.text = QTextEdit()
        self.text.setReadOnly(True)

        layout.addWidget(self.text)

    def set_prompt(self, prompt: str):
        """Display the generated prompt."""
        self.text.setPlainText(prompt)