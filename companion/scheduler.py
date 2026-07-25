import random

from companion.state import CompanionState


class Scheduler:

    def __init__(self):

        self.elapsed = 0.0

        self.next_change = self.random_interval()

    def random_interval(self):

        return random.uniform(8.0, 15.0)

    def update(self, dt):

        self.elapsed += dt

        if self.elapsed >= self.next_change:

            self.elapsed = 0

            self.next_change = self.random_interval()

            return True

        return False

    def choose_next_state(self, current_state):

        choices = [

            CompanionState.IDLE,

            CompanionState.WALK,

            CompanionState.RUN

        ]

        if current_state in choices:

            choices.remove(current_state)

        return random.choice(choices)