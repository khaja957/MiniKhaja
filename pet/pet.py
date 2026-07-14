from PySide6.QtCore import QObject, QPoint, Signal

from animation.animation_engine import AnimationEngine
from animation.sprite_loader import SpriteLoader
from movement.movement_engine import MovementEngine
from pet.direction import Direction
from pet.state import PetState
from pet.behaviors.walk_behavior import WalkBehavior


class Pet(QObject):
    """
    Represents the character's behavior.

    This class owns the animation and movement engines
    and exposes simple methods like idle() and walk_to().
    """
    frame_changed = Signal(object, bool)

    def __init__(self):
        super().__init__()

        # Create Components 
        self.loader = SpriteLoader()
        self.animation = AnimationEngine()
        self.movement = MovementEngine()
        self.direction = Direction.RIGHT
        self.walk_behavior = WalkBehavior(self)

        # State
        self.state = PetState.IDLE

        #Connect Signals
        self.animation.frame_changed.connect(self.on_frame_changed)
        self.movement.movement_finished.connect(self.on_walk_finished)


    def change_state(self, state: PetState):

        if self.state == state:
            return

        self.state = state

        animation_map = {PetState.IDLE: "idle",
                         PetState.WALK: "walk",
                         PetState.TALK: "talk",
                         PetState.DRINK: "drink",
                         PetState.WAVE: "wave",
                         PetState.SLEEP: "sleep",
                        }

        animation_name = animation_map.get(state)
        if animation_name:
            self.play_animation(animation_name)

    def play_animation(self, name: str):
        frames = self.loader.load(name)
        self.animation.play(frames)

    def idle(self):
        """Play the idle animation."""
        self.change_state(PetState.IDLE)

    def walk_to(self, start: QPoint, target: QPoint):
        """Move the pet to a new position."""
        if target.x() > start.x():
            self.direction = Direction.RIGHT
        else:
            self.direction = Direction.LEFT

        self.change_state(PetState.WALK)
        self.walk_behavior.execute(start, target)

    def on_walk_finished(self):
        self.change_state(PetState.IDLE)

    def on_frame_changed(self, pixmap):
        flip = self.direction == Direction.LEFT
        self.frame_changed.emit(pixmap, flip)        