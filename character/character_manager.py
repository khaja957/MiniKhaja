import json
from dataclasses import asdict
from pathlib import Path

from character.registry import CharacterRegistry
from studio.settings import StudioSettings


class CharacterManager:

    @staticmethod
    def lock(name: str):

        profile = CharacterRegistry.get(name)

        output = (
            StudioSettings.ASSETS
            / "character"
        )

        output.mkdir(parents=True, exist_ok=True)

        file = output / f"{name}.json"

        with open(file, "w", encoding="utf-8") as f:
            json.dump(
                asdict(profile),
                f,
                indent=4,
                ensure_ascii=False
            )

        return file