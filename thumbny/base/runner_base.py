from typing import Optional


class RunnerBase():
    def __init__(self, json_string: Optional[str] = None):
        if json_string:
            self.model = self.build(json_string)

    def build(self, json_string: str) -> None:
        return NotImplementedError()

    def execute(self) -> None:
        raise NotImplementedError()
