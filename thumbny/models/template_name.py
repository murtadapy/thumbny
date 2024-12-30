from __future__ import annotations

from typing import Dict
from typing import Any

from dataclasses import dataclass


@dataclass
class TemplateNameModel:
    name: str

    @classmethod
    def make(cls, data: Dict[str, Any]) -> TemplateNameModel:
        """Create the model

        Args:
            data (Dict[str, Any]): dictionary data

        Returns:
            TagModel: model
        """
        return cls(name=data.get("name"))
