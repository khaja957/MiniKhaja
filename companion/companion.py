from pathlib import Path

from animation.loader import AnimationLoader

from companion.state import CompanionState
from companion.state_machine import StateMachine
from companion.scheduler import Scheduler
from companion.brain import Brain


class Companion:

    def __init__(self, player):

        self.player = player

        self.loader = AnimationLoader(

            Path("assets/minikhaja")

        )

        self.scheduler = Scheduler()

        self.brain = Brain()

        self.state_machine = StateMachine(player)

        self.animations = {}

    def load(self):

        for state in CompanionState:

            try:

                animation = self.loader.load(state.value)

                self.animations[state] = animation

                print(f"[OK] Loaded {state.value}")

            except FileNotFoundError:

                print(f"[INFO] Animation '{state.value}' not found. Skipping.")

    def start(self):

        if not self.animations:

            print()

            print("ERROR: No animations loaded.")

            return

        self.change_state(CompanionState.IDLE)

    def update(self, dt):

        if self.scheduler.update(dt):

            next_state = self.scheduler.choose_next_state(self.state_machine.current_state)

            self.change_state(next_state)

    def change_state(self, state):

        if self.state_machine.current_state == state:
            return

        animation = self.animations.get(state)

        if animation is None:

            return

        self.state_machine.current_state = state

        self.state_machine.change(animation)