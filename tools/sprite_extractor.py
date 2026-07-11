import sys
from pathlib import Path
from image_canvas import ImageCanvas

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from utils.file_helper import get_next_sprite_name
from animation_player import AnimationPlayer

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QWidget,
    QScrollArea,
)

class SpriteExtractor(QWidget):

    def __init__(self):
        super().__init__()
        self.animation_combo = QComboBox()

        self.animation_combo.addItems(["idle","walk","wave","talk","drink","sleep","think","sit"])

        self.image_label = ImageCanvas()
        self.next_sprite_label = QLabel()
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.image_label)
        self.scroll_area.setWidgetResizable(False)

        ##Animation play area
        self.preview_label = QLabel()
        self.preview_label.setFixedSize(250, 250)
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setStyleSheet("""border:1px solid gray;background:white;""")

        self.animation_player = AnimationPlayer()
        self.animation_player.frame_changed.connect(
            self.preview_label.setPixmap
        )

        ##Animation player buttons
        self.play_button = QPushButton("▶ Play")
        self.stop_button = QPushButton("■ Stop")
        self.play_button.clicked.connect(
             self.play_animation
        )
        self.stop_button.clicked.connect(
                self.animation_player.stop
        )

        ##Buttons
        self.open_button = QPushButton(
            "Open Character Sheet"
        )

        self.save_button = QPushButton("Save Sprite")

        self.open_button.clicked.connect(
            self.open_image
        )

        self.animation_combo.currentTextChanged.connect(
             self.update_next_sprite_label
        )

        self.save_button.clicked.connect(
           self.save_sprite
        )

        
        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        ##Building the Top bar 
        toolbar_layout = QHBoxLayout()
        toolbar_layout.addWidget(QLabel("Animation"))
        toolbar_layout.addWidget(self.animation_combo)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.next_sprite_label)

        ## Building Left Panel - This will contain Character sheet
        left_panel = QVBoxLayout()
        left_panel.addWidget(self.scroll_area)

        ## Building Right Panel for Animation preview
        right_panel = QVBoxLayout()
        right_panel.addWidget(QLabel("Animation Preview"))
        right_panel.addWidget(self.preview_label)
        right_panel.addWidget(self.play_button)
        right_panel.addWidget(self.stop_button)
        right_panel.addStretch()
        
        ## Combine Left and Right Panels 
        top_layout.addLayout(left_panel, 3)
        top_layout.addLayout(right_panel, 1)

        ## Building Bottom Bar 
        bottom_layout.addWidget(self.open_button)
        bottom_layout.addWidget(self.save_button)

        ## Final Assembly of the panels 
        main_layout.addLayout(toolbar_layout)
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)
        self.setLayout(main_layout)

        self.setWindowTitle(
            "Mini Khaja Sprite Extractor"
        )

        self.resize(1200, 900)

        self.update_next_sprite_label()         ## Update the lable at the end of __init__ ()

    def open_image(self):

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Character Sheet",
            "",
            "PNG Files (*.png)"
        )

        if not file_name:
            return

        pixmap = QPixmap(file_name)

        self.image_label.set_image(pixmap)

        self.image_label.adjustSize()    

    def save_sprite(self):

        rect = self.image_label.get_selection()

        if rect.isNull():
            return

        pixmap = self.image_label.pixmap_image

        cropped = pixmap.copy(rect)

        animation = self.animation_combo.currentText()

        save_folder = (
            Path("assets")/ "sprites"/ "character" / animation
        )

        filename = get_next_sprite_name(save_folder, animation)
        save_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        save_path = save_folder / filename
        
        cropped.save(str(save_path))

        print(f"Saved: {save_path}")
        self.update_next_sprite_label()     ## Update the label after every save

    def update_next_sprite_label(self):

        animation = self.animation_combo.currentText()

        folder = ( Path("assets") / "sprites" / "character" / animation )

        filename = get_next_sprite_name(folder,animation)

        self.next_sprite_label.setText(f"Next Sprite: {filename}")

    def play_animation(self):

        animation = self.animation_combo.currentText()
        folder = (Path("assets") / "sprites" / "character" / animation)
        self.animation_player.load(folder)
        self.animation_player.play(fps=6)


def main():

    app = QApplication(sys.argv)

    window = SpriteExtractor()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()            