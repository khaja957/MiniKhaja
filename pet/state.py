from enum import Enum, auto


class PetState(Enum):
    IDLE = auto()
    WALK = auto()
    TALK = auto()
    DRINK = auto()
    SLEEP = auto()
    WAVE = auto()