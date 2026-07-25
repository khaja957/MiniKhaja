class StateMachine:

    def __init__(self, player):

        self.player = player

        self.current_state = None

    def change(self, animation):

        if self.current_state == animation.name:

            return

        self.current_state = animation.name

        print(f"State -> {self.current_state}")

        self.player.play(animation)