from character.animation.animation_library import ANIMATIONS


class AnimationDirector:

    def __init__(self, animation_engine):
        self.engine = animation_engine

    def play(self, animation_type, frames):
        """
        Play an animation using its specification.
        """
        spec = ANIMATIONS[animation_type]

        self.engine.fps = spec.fps

        self.engine.play(
            frames=frames,
            loop=spec.looping,
            fps=spec.fps
        )