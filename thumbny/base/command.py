from typing import Optional

from thumbny.templates_manager import TemplateManager


class CommandBase:
    def __init__(self, model: Optional[object] = None) -> None:
        if model:
            self.validate()

        self.tm = TemplateManager()

    def validate(self) -> None:
        return NotImplemented()

    def execute() -> None:
        raise NotImplementedError()
