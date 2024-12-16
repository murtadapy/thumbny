from typing import List
from dataclasses import dataclass

from thumbny.models.shared import TagModel
from thumbny.models.validation import check_required_fields


@dataclass
class FillerModel:
    template_key: str
    labels: List[TagModel]

    def __post_init__(self):
        check_required_fields(self)
