from dataclasses import dataclass


@dataclass
class ChromaKeySettings:

    lower_h: int = 35
    lower_s: int = 40
    lower_v: int = 40

    upper_h: int = 90
    upper_s: int = 255
    upper_v: int = 255

    blur_size: int = 5

    kernel_size: int = 3

    despill: bool = True

    feather_edges: bool = True