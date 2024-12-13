from typing import Optional

from thumbny.base import RunnerBase
from thumbny.commands import Create


class CreateRunner(RunnerBase):
    def __init__(self, json_string: Optional[str] = None):
        super().__init__(json_string)

    def build(self, json_string):
        return super().build(json_string)

    def execute(self):
        return super().execute()
