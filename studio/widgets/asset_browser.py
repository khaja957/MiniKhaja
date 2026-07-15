from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QListWidget, QVBoxLayout, QWidget


class AssetBrowser(QWidget):

    asset_selected = Signal(Path)

    def __init__(self):
        super().__init__()

        self.assets_dir = Path("assets/source/images")

        layout = QVBoxLayout(self)

        self.list = QListWidget()

        layout.addWidget(self.list)

        self.list.itemClicked.connect(self.on_item_clicked)

        self.refresh()

    def refresh(self):

        self.list.clear()

        self.assets_dir.mkdir(parents=True, exist_ok=True)

        for file in sorted(self.assets_dir.glob("*")):

            if file.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"):
                self.list.addItem(file.name)

    def on_item_clicked(self, item):

        path = self.assets_dir / item.text()

        self.asset_selected.emit(path)