from random import randint, choice
from pet.state import PetState
from PySide6.QtCore import QObject, QPoint, QTimer


class PetScheduler(QObject):
    """
    Periodically asks the pet to perform autonomous actions.
    """

    def __init__(self, pet, desktop_window):
        super().__init__()

        self.pet = pet
        self.window = desktop_window

        self.timer = QTimer()
        self.timer.timeout.connect(self.choose_next_action)

        # Every 8 seconds for now
        self.timer.start(8000)

    def choose_next_action(self):

        # Don't interrupt an active behavior
        if self.pet.state != PetState.IDLE:
            return

        action = choice(["idle", "walk", "walk", "walk"])

        if action == "idle":
            return

        screen = self.window.screen().availableGeometry()

        margin = 20

        x = randint(margin, screen.width() - self.window.width() - margin )

        target = QPoint( x,  self.window.y() )

        self.pet.walk_to( self.window.pos(), target)