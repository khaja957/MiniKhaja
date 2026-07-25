from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np

from models.bounding_box import BoundingBox
from models.chromakey_settings import ChromaKeySettings
from models.animation_asset import AnimationAsset


@dataclass
class AnimationProject:

    # Input
    video_path: Path

    output_folder: Path

    # Video Info
    fps: float = 0.0
    frame_count: int = 0

    # Frames
    frames: list[np.ndarray] = field(default_factory=list)

    # Analysis
    bounds: list[BoundingBox] = field(default_factory=list)

    normalized_width: int = 0
    normalized_height: int = 0


    # Settings
    chromakey: ChromaKeySettings = field(
        default_factory=ChromaKeySettings
    )

    # Metadata
    metadata: dict = field(default_factory=dict)

    # Final Asset
    asset: Optional[AnimationAsset] = None