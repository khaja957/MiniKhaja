from dataclasses import dataclass


@dataclass
class Animations:

    idle: str = "idle"

    walk: str = "walk"

    wave: str = "wave"

    talk: str = "talk"

    drink: str = "drink"

    sleep: str = "sleep"