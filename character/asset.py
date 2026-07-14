from dataclasses import dataclass
from pathlib import Path


@dataclass
class CharacterAsset:

    name: str

    asset_type: str

    file_path: Path

    prompt: str