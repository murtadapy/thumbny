import re

from thumbny.base import CommandBase
from thumbny.exceptions import NotValidColor
from thumbny.models import CreateModel


HEX_REGEX = r'^#[0-9a-fA-F]{6}$'


class CreateCommand(CommandBase):
    def __init__(self, model: CreateModel):
        super().__init__(model)

    def validate(self):
        if self.model.background_color:
            if re.match(HEX_REGEX, self.model.background_color):
                raise NotValidColor("Not a valid background color")

        for label in self.model.labels:
            print(label)
            if not re.match(HEX_REGEX, label.font_color):
                raise NotValidColor("Not a valid font color")

    def execute(self):
        self.tm.create(self.model)
        print(f"{self.model.key} template has been created successfully")
