from typing import List
from typing import Optional
from dataclasses import dataclass

from thumbny.models.shared import TagModel
from thumbny.models.validation import check_required_fields
from thumbny.models.validation import check_spaces
from thumbny.models.validation import check_hex_color


@dataclass
class LabelModel:
    key: str
    content: str
    position: TagModel
    alignment: Optional[str]
    font_color: str
    font_size: int
    font_family: Optional[str]

    def __post_init__(self):
        check_required_fields(self)


@dataclass
class TemplateModel:
    key: str
    name: str
    width: int
    height: int
    background_color: str
    labels: List[LabelModel]

    def __post_init__(self):
        check_required_fields(self)
        check_spaces("key", self.key)
        check_hex_color("background_color", self.background_color)
