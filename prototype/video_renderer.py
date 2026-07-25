from pathlib import Path

from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QGraphicsVideoItem
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView


class VideoRenderer(QGraphicsView):

    def __init__(self):

        super().__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.video = QGraphicsVideoItem()
        self.scene.addItem(self.video)

        self.player = QMediaPlayer(self)

        self.audio = QAudioOutput(self)

        self.player.setAudioOutput(self.audio)

        self.audio.setVolume(0)

        self.player.setVideoOutput(self.video)

    def play(self, video_path):

        self.player.setSource(
            QUrl.fromLocalFile(str(Path(video_path).resolve()))
        )

        self.player.play()