from dataclasses import dataclass

from thumbny.models.validation import check_required_fields


@dataclass
class TagModel:
    key: str
    value: str

    def __post_init__(self):
        check_required_fields(self)
