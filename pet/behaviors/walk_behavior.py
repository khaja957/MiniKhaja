from PySide6.QtCore import QPoint

from pet.state import PetState


class WalkBehavior:

    def __init__(self, pet):
        self.pet = pet

    def execute(self, start: QPoint, target: QPoint):

        self.pet.change_state(PetState.WALK)

        self.pet.movement.move_to(start, target)