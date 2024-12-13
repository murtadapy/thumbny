from typing import Optional

from thumbny.base import RunnerBase
from thumbny.commands import InfoCommand


class InfoRunner(RunnerBase):
    def __init__(self, json_string: Optional[str] = None) -> None:
        super().__init__(json_string)

    def build(self, json_dict: dict) -> None:
        return super().build(json_dict)

    def execute(self) -> None:
        return super().execute()
