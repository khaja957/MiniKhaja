from PySide6.QtCore import QObject, QTimer, Qt
from PySide6.QtGui import QPixmap
from config.settings import SPRITE_SCALE

class AnimationPlayer(QObject):

    def __init__(self, window):

        super().__init__()

        # Window
        self.window = window

        # Sprite renderer (QGraphicsPixmapItem)
        self.sprite = window.sprite

        # Current animation
        self.animation = None

        # Current frame index
        self.current_frame = 0

        # Playback timer
        self.timer = QTimer()

        self.timer.timeout.connect(self.next_frame)

    # ---------------------------------------------------------

    def play(self, animation):

        if animation is None:
            return

        # Avoid restarting the same animation
        #if self.animation == animation:
         #   return

        self.animation = animation

        self.current_frame = 0

        interval = int(1000 / animation.fps)

        self.timer.start(interval)

        self.next_frame()

    # ---------------------------------------------------------

    def stop(self):

        self.timer.stop()

        self.animation = None

        self.current_frame = 0

    # ---------------------------------------------------------

    def next_frame(self):

        if self.animation is None:
            return

        if len(self.animation.frames) == 0:
            return

        pixmap = self.animation.frames[self.current_frame]

        if pixmap.isNull():
            return        

        scaled = pixmap.scaled(int(pixmap.width() * SPRITE_SCALE), int(pixmap.height() * SPRITE_SCALE),  Qt.KeepAspectRatio,  Qt.SmoothTransformation,)

        self.sprite.setPixmap(scaled)

        #self.sprite.setPixmap(pixmap)

        self.window.fit_to_pixmap()

        self.current_frame += 1

        if self.current_frame >= len(self.animation.frames):
            self.current_frame = 0

    # ---------------------------------------------------------

    def is_playing(self):

        return self.timer.isActive()