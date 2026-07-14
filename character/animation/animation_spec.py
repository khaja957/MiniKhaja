from dataclasses import dataclass

from .animation_type import AnimationType


@dataclass
class AnimationSpec:

    animation: AnimationType

    fps: int

    duration: float

    looping: bool

    description: str

    body_motion: str

    head_motion: str

    arm_motion: str

    facial_expression: str