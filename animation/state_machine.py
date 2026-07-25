class StateMachine:

    def __init__(self, player):

        self.player = player

        self.state = None

    def change(self, animation):

        print(f"Playing {animation.name}")

        self.player.play(animation)