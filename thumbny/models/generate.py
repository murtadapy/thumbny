from typing import List
from dataclasses import dataclass

from thumbny.models.validation import check_required_fields


@dataclass
class TagGenerateModel:
    key: str
    value: str

    def __post_init__(self):
        check_required_fields(self)


@dataclass
class GenerateModel:
    template_key: str
    labels: List[TagGenerateModel]

    def __post_init__(self):
        check_required_fields(self)
