from dataclasses import dataclass, field


@dataclass
class AnimationAsset:

    # Animation information
    name: str = ""

    fps: float = 24.0

    loop: bool = True

    frame_count: int = 0

    # Canvas
    canvas_width: int = 0

    canvas_height: int = 0

    # Pivot
    pivot_x: int = 0

    pivot_y: int = 0

    # Frame filenames
    frames: list[str] = field(default_factory=list)