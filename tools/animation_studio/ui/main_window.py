from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QFileDialog,
    QLabel,
    QVBoxLayout,
)

from pathlib import Path

from models.animation_project import AnimationProject
from pipeline.extractor import FrameExtractor
from pipeline.builder import StudioPipelineBuilder
from pipeline.context import PipelineContext

class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("MiniKhaja Animation Studio")

        self.resize(500, 220)

        self.video_path = ""

        self.label = QLabel("No video selected")

        self.select_button = QPushButton("Select MP4")

        self.process_button = QPushButton("Process")

        layout = QVBoxLayout()

        layout.addWidget(self.label)

        layout.addWidget(self.select_button)

        layout.addWidget(self.process_button)

        self.setLayout(layout)

        self.select_button.clicked.connect(self.select_video)

        self.process_button.clicked.connect(self.process_video)

    def select_video(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select Video",
            "",
            "Videos (*.mp4)"
        )

        if filename:

            self.video_path = filename

            self.label.setText(filename)

    def process_video(self):

        project = AnimationProject(
                    video_path=Path(self.video_path),
                    output_folder=Path("output")
                 )

        extractor = FrameExtractor()

        extractor.extract(project)

        pipeline = (StudioPipelineBuilder().build())

        context = PipelineContext(project)

        pipeline.execute(context)