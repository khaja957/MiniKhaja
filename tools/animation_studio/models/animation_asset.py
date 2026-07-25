from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class AnimationAsset:

    name: str

    fps: float

    frame_count: int

    canvas_width: int

    canvas_height: int


    frame_paths: list[Path] = field(default_factory=list)