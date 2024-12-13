from thumbny.templates_manager import TemplateManager
from thumbny.base import CommandBase


class Delete(CommandBase):
    def __init__(self,
                 name: str) -> None:
        self.name = name
        self.template_manager = TemplateManager()

    def execute(self) -> None:
        self.template_manager.delete(self.name)
        print(f"{self.name} template has been deleted successfully")
