import re

from thumbny.base import CommandBase
from thumbny.exceptions import NotValidColor
from thumbny.models import CreateModel


HEX_REGEX = r'^#[0-9a-fA-F]{6}$'


class CreateCommand(CommandBase):
    def __init__(self, model: CreateModel):
        super().__init__(model)
        self.model = model

    def validate(self):
        if not re.match(HEX_REGEX, self.model.background_color):
            raise NotValidColor("Not a valid background color")

        for label in self.model.labels:
            if not re.match(HEX_REGEX, label.font_color):
                raise NotValidColor("Not a valid font color")

    def execute(self):
        self.tm.create(key=self.model.key,
                       name=self.model.name,
                       width=self.model.width,
                       height=self.model.height,
                       background_color=self.model.background_color,
                       font_color=self.model.font_color,
                       font_size=self.model.font_size,
                       font_family=self.model.font_family)
        print(f"{self.name} template has been created successfully")
