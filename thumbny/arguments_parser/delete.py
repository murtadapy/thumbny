from typing import Dict
from typing import Any
from typing import Optional

from thumbny.base import RunnerBase
from thumbny.commands import DeleteCommand
from thumbny.models import TemplateNameModel


class DeleteRunner(RunnerBase):
    def __init__(self, arguments: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(arguments)

    def build(self, json_dict: Dict[str, Any]) -> TemplateNameModel:
        """Build data model

        Args:
            json_dict (Dict[str, Any]): json data

        Returns:
            TemplateNameModel: data model
        """
        return TemplateNameModel.make(json_dict)

    def execute(self) -> None:
        """Execute the delete command"""
        command = DeleteCommand(self.model)
        return command.execute()
