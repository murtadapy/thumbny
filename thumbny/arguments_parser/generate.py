from typing import Optional

from thumbny.base import RunnerBase
from thumbny.commands import GenerateCommand
from thumbny.models import FillerModel
from thumbny.models import TagModel


class GenerateRunner(RunnerBase):
    def __init__(self, json_string: Optional[str] = None) -> None:
        super().__init__(json_string)

    def build(self, json_dict: dict) -> FillerModel:
        labels = []
        for label in json_dict.get("labels", []):
            labels.append(TagModel(key=label.get("key"),
                                           value=label.get("value")))

        return FillerModel(template_key=json_dict.get("template_key"),
                             labels=labels)

    def execute(self) -> None:
        command = GenerateCommand()
        command.execute()
