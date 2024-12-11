from typing import Tuple

from dataclasses import dataclass


@dataclass
class Template:
    name: str
    width: str
    height: int
    background_color: Tuple[int]
    font_color: Tuple[int]
    font_size: int
    font_family: str
