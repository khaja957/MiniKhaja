from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
)

from studio.widgets.toolbar import Toolbar
from studio.asset_pipeline import AssetPipeline
from studio.widgets.prompt_panel import PromptPanel
from studio.widgets.preview_panel import PreviewPanel
from studio.widgets.status_bar import StudioStatusBar
from character.registry import CharacterRegistry
from studio.prompt_builder import PromptBuilder
from studio.widgets.asset_browser import AssetBrowser
from character.character_manager import CharacterManager

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
        self.asset_browser = AssetBrowser()

        content = QHBoxLayout()

        self.prompt_panel = PromptPanel()
        self.preview_panel = PreviewPanel()

        self.toolbar.generate.clicked.connect(self.generate_asset)
        self.toolbar.lock_character.clicked.connect(self.lock_character)
        self.asset_browser.asset_selected.connect(self.preview_panel.show_image)
        self.toolbar.refresh.clicked.connect(self.asset_browser.refresh)

        # Load Mini Khaja profile
        profile = CharacterRegistry.get("mini_khaja")

        # Build the prompt
        builder = PromptBuilder(profile)

        prompt = builder.build_idle_prompt()

        # Show it in the UI
        self.prompt_panel.set_prompt(prompt)

        content.addWidget(self.prompt_panel, 1)
        content.addWidget(self.preview_panel, 2)
        content.addWidget(self.asset_browser, 1)

        main_layout.addWidget(self.toolbar)
        main_layout.addLayout(content)
        main_layout.addWidget(self.status)
    
    def generate_asset(self):

        self.status.set_status("Generating...")

        profile = CharacterRegistry.get("mini_khaja")

        builder = PromptBuilder(profile)

        prompt = builder.build_idle_prompt()

        pipeline = AssetPipeline()

        asset = pipeline.generate(name=profile.name, prompt=prompt)

        self.preview_panel.show_image(asset.file_path)

        self.status.set_status("Generation Complete")

    def lock_character(self):

        CharacterManager.lock("mini_khaja")

        self.status.set_status("Character locked successfully.")