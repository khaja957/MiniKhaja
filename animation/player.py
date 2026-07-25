from PySide6.QtCore import QObject, QTimer, Qt


class AnimationPlayer(QObject):

    def __init__(self, pixmap_item):

        super().__init__()

        self.pixmap_item = pixmap_item

        self.animation = None

        self.current_frame = 0

        self.scale = 0.45

        self.timer = QTimer()

        self.timer.timeout.connect(self.next_frame)

        self.window_fitted = False

    def play(self, animation):

        self.animation = animation

        self.current_frame = 0

        self.window_fitted = False

        interval = int(1000 / animation.fps)

        self.timer.start(interval)

        self.next_frame()

    def next_frame(self):

        if self.animation is None:
            return

        if self.current_frame >= self.animation.frame_count:

            if self.animation.loop:
                self.current_frame = 0
            else:
                self.timer.stop()
                return

        pixmap = self.animation.frames[self.current_frame]

        scaled = pixmap.scaled(

            int(pixmap.width() * self.scale),

            int(pixmap.height() * self.scale),

            Qt.KeepAspectRatio,

            Qt.SmoothTransformation

        )

        self.pixmap_item.setPixmap(scaled)

        scene = self.pixmap_item.scene()

        scene.setSceneRect(self.pixmap_item.boundingRect())

        if not self.window_fitted:

            view = scene.views()[0]

            window = view.window()

            window.fit_to_pixmap()

            self.window_fitted = True

        self.current_frame += 1