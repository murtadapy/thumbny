from typing import List

from dataclasses import dataclass


@dataclass
class TagCreateModel:
    key: str
    value: str


@dataclass
class LabelCreateModel:
    key: str
    content: str
    position: TagCreateModel
    alignment: str
    font_color: str
    font_size: str
    font_family: str


@dataclass
class CreateModel:
    key: str
    name: str
    width: str
    height: int
    background_color: str
    labels: List[LabelCreateModel]
