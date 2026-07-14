from dataclasses import dataclass

from character.appearance import Appearance
from character.personality import Personality
from character.animations import Animations


@dataclass
class CharacterProfile:

    name: str

    appearance: Appearance

    personality: Personality

    animations: Animations