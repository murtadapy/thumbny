from typing import List

from dataclasses import dataclass


@dataclass
class KeyValue:
    key: str
    value: str


@dataclass
class Text:
    content: str
    position: KeyValue
    alignment: str
    font_color: str
    font_size: str
    font_family: str


@dataclass
class CreateModel:
    name: str
    width: str
    height: int
    background_color: str
    text: List[Text]
