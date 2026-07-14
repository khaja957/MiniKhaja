from .animation_spec import AnimationSpec
from .animation_type import AnimationType


ANIMATIONS = {

    AnimationType.IDLE:

        AnimationSpec(

            animation=AnimationType.IDLE,

            fps=24,

            duration=3,

            looping=True,

            description="Standing naturally",

            body_motion="gentle breathing",

            head_motion="subtle sway",

            arm_motion="tiny relaxed movement",

            facial_expression="friendly smile"
        ),

    AnimationType.WALK:

        AnimationSpec(

            animation=AnimationType.WALK,

            fps=24,

            duration=2,

            looping=True,

            description="Walking naturally",

            body_motion="body leans slightly forward",

            head_motion="gentle bob",

            arm_motion="smooth arm swing",

            facial_expression="happy"
        )
}