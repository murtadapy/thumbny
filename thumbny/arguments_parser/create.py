from typing import Optional

from thumbny.base import RunnerBase
from thumbny.commands import CreateCommand
from thumbny.models import TagCreateModel
from thumbny.models import LabelCreateModel
from thumbny.models import CreateModel


class CreateRunner(RunnerBase):
    def __init__(self, json_string: Optional[str] = None) -> None:
        super().__init__(json_string)

    def build(self, json_dict: dict) -> CreateModel:
        labels = []

        for label in json_dict.get("labeles", []):
            position = TagCreateModel(key=label.get("position", "key"),
                                      value=label.get("position", "value"))

            label = LabelCreateModel(key=label.get("key"),
                                     content=label.get("content"),
                                     position=position,
                                     alignment=label.get("alignment"),
                                     font_color=label.get("font-color"),
                                     font_size=label.get("font-size"),
                                     font_family=label.get("font-family"))
            labels.append(label)

        return CreateModel(key=json_dict.get("key"),
                           name=json_dict.get("name"),
                           width=json_dict.get("width"),
                           height=json_dict.get("height"),
                           background_color=json_dict.get("background-color"),
                           labels=labels)

    def execute(self) -> None:
        command = CreateCommand(self.model)
        command.execute()
