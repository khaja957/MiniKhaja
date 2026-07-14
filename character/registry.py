from character.profiles.mini_khaja import mini_khaja


class CharacterRegistry:

    _characters = {
        "mini_khaja": mini_khaja
    }

    @classmethod
    def get(cls, name: str):
        return cls._characters[name]

    @classmethod
    def list(cls):
        return list(cls._characters.keys())