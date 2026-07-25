class Scheduler:

    def __init__(self):

        self.elapsed = 0

    def update(self, dt):

        self.elapsed += dt