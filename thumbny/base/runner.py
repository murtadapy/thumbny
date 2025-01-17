from typing import Dict
from typing import Any
from typing import Optional

import json
from dataclasses import dataclass


class RunnerBase:
    def __init__(self, arguments: Optional[Dict[str, Any]] = None) -> None:
        self.model = None
        self.arguments = arguments

        data = self.arguments.get("data", None)
        if data:
            json_dict = json.loads(data)
            self.model = self.build(json_dict)

    def build(self, json_dict: Dict[str, Any]) -> dataclass:
        """Build data model

        Args:
            json_dict (Dict[str, Any]): json data

        Returns:
            dataclass: data model
        """
        return NotImplementedError()

    def run(self) -> None:
        """Run the command"""
        raise NotImplementedError()
