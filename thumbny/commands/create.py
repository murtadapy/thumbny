import re

from thumbny.templates_manager import TemplateManager
from thumbny.base import CommandBase
from thumbny.exceptions import NotValidColor
from thumbny.models import CreateModel


HEX_REGEX = r'^#[0-9a-fA-F]{6}$'


class CreateCommand(CommandBase):
    def __init__(self, model: CreateModel) -> None:
        self.model = model
        self.template_manager = TemplateManager()

    def _validate(self) -> None:
        if not re.match(HEX_REGEX, self.background_color):
            raise NotValidColor("Not a valid background color")

        if not re.match(HEX_REGEX, self.font_color):
            raise NotValidColor("Not a valid font color")

    def execute(self) -> None:
        self.template_manager.create(name=self.name,
                                     width=self.width,
                                     height=self.height,
                                     background_color=self.background_color,
                                     font_color=self.font_color,
                                     font_size=self.font_size,
                                     font_family=self.font_family)
        print(f"{self.name} template has been created successfully")
