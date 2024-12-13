from typing import Optional

import json


class RunnerBase():
    def __init__(self, json_string: Optional[str] = None):
        if json_string:
            json_dict = json.loads(json_string)
            self.model = self.build(json_dict)

    def build(self, json_dict: dict) -> None:
        return NotImplementedError()

    def execute(self) -> None:
        raise NotImplementedError()
