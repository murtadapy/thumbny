from typing import Optional

from thumbny.templates_manager import TemplateManager


class CommandBase:
    def __init__(self, model: Optional[object] = None) -> None:
        self.model = model
        self.tm = TemplateManager()

    def execute() -> None:
        raise NotImplementedError()
