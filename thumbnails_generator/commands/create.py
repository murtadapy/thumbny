import re

from thumbnails_generator.templates_manager import TemplateManager
from thumbnails_generator.abstracts import CommandBase
from thumbnails_generator.exceptions import NotValidColor


HEX_REGEX = r'^#[0-9a-fA-F]{6}$'


class Create(CommandBase):
    def __init__(self,
                 name: str,
                 width: str,
                 height: str,
                 background_color: str,
                 font_color: str,
                 font_path: str) -> None:
        self.name = name
        self.width = width
        self.height = height
        self.background_color = background_color
        self.font_color = font_color
        self.font_path = font_path

        self.template_manager = TemplateManager()

    def _validate(self) -> None:
        if not re.match(HEX_REGEX, self.background_color):
            raise NotValidColor("Not a valid background color")

        if not re.match(HEX_REGEX, self.font_color):
            raise NotValidColor("Not a valid font color")

    def execute(self) -> None:
        self._validate()
        self.template_manager.create(name=self.name,
                                     width=self.width,
                                     height=self.height,
                                     background_color=self.background_color,
                                     font_color=self.font_color,
                                     font_path=self.font_path)
        print(f"{self.name} template has been created successfully")
