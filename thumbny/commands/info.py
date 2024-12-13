from thumbny.templates_manager import TemplateManager
from thumbny.base import CommandBase


class Info(CommandBase):
    def __init__(self, name: str) -> None:
        self.name = name
        self.template_manager = TemplateManager()

    def execute(self) -> None:
        details = self.template_manager.get_template_info(self.name)
        print("="*40)
        print(f"{'Key':<20} {'Value'}")
        print("="*40)
        for x, y in details.items():
            print(f"{x:<20} {y}")