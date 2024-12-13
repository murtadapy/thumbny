from typing import Optional

from thumbny.base import RunnerBase
from thumbny.commands import Delete


class DeleteRunner(RunnerBase):
    def __init__(self, json_string: Optional[str] = None) -> None:
        super().__init__(json_string)

    def build(self, json_string) -> None:
        return super().build(json_string)

    def execute(self) -> None:
        return super().execute()
