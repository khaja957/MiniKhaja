from character.profile import CharacterProfile


class PromptBuilder:

    def __init__(self, profile: CharacterProfile):
        self.profile = profile

    def _base_prompt(self) -> str:

        appearance = self.profile.appearance

        return f"""
Create a highly detailed cute chibi character.

Character Name:
{self.profile.name}

Appearance:
- Same character in every generation
- {appearance.hair}
- {appearance.beard}
- {appearance.hoodie}
- {appearance.pants}
- {appearance.shoes}
- {appearance.eye_color} eyes
- {appearance.skin_tone} skin tone

Style:
- Pixar-quality illustration
- Soft lighting
- Rounded proportions
- Large expressive eyes
- Clean outlines
- Vibrant colors

Background:
Transparent PNG.

Keep the character identity perfectly consistent.
"""

    def build_idle_prompt(self):

        return self._base_prompt() + """

Action:
Standing naturally.

Animation Notes:
Gentle breathing.
Natural posture.
Relaxed arms.
Friendly smile.
"""

    def build_walk_prompt(self):

        return self._base_prompt() + """

Action:
Walking.

Animation Notes:
Left foot forward.
Right arm forward.
Natural body lean.
Arms swinging.
Head gently bobbing.
"""

    def build_wave_prompt(self):

        return self._base_prompt() + """

Action:
Standing and waving.

Animation Notes:
Smile.
Raise right hand.
Friendly greeting.
"""

    def build_drink_prompt(self):

        return self._base_prompt() + """

Action:
Holding a water bottle.

Animation Notes:
Drink naturally.
Smile afterwards.
"""

    def build_sleep_prompt(self):

        return self._base_prompt() + """

Action:
Sleeping peacefully.

Animation Notes:
Eyes closed.
Gentle breathing.
Relaxed posture.
"""