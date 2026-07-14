from character.appearance import Appearance
from character.personality import Personality
from character.animations import Animations
from character.profile import CharacterProfile


mini_khaja = CharacterProfile(

    name="Mini Khaja",

    appearance=Appearance(

        hair="short black hair",

        beard="trimmed beard",

        hoodie="blue hoodie",

        pants="dark jeans",

        shoes="white sneakers",

        eye_color="brown",

        skin_tone="medium"
    ),

    personality=Personality(

        friendliness=0.95,

        curiosity=0.85,

        energy=0.75,

        humor=0.90,

        patience=0.95
    ),

    animations=Animations()
)