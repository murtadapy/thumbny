from typing import Optional
from typing import List

import os
import sys
import json
import re

from thumbnails_generator.abstracts import CommandBase
from thumbnails_generator.exceptions import TemplateExist
from thumbnails_generator.exceptions import NotValidColor


HEX_REGEX = r'^#[0-9a-fA-F]{6}$'


class Create(CommandBase):
    def __init__(self,
                 *,
                 name: str,
                 width: Optional[str],
                 height: Optional[str],
                 background_color: Optional[str],
                 font_color: Optional[str],
                 font: Optional[str]) -> None:
        self.name = name
        self.width = width
        self.height = height
        self.background_color = background_color
        self.font_color = font_color
        self.font = font

        self.templates_path = os.path.join(sys.path[0],
                                           "thumbnails_generator",
                                           "templates")

        self.template_path = os.path.join(self.templates_path,
                                          self.name)

    def _get_all_templates(self) -> List[str]:
        return os.listdir(self.templates_path)

    def _create_folder(self) -> None:
        if self.name in self._get_all_templates():
            raise TemplateExist(f"Template {self.name} is already exist")

        path = os.path.join(self.template_path)
        os.mkdir(path)

    def _create_config(self) -> None:
        config = {
            "name": self.name,
            "width": self.width,
            "height": self.height,
            "background_color": self.background_color,
            "font_color": self.font_color,
            "font": self.font
        }

        path = os.path.join(self.template_path, "config.json")
        with open(path, "w") as f:
            json.dump(config, f, indent=4)

    def _validate(self) -> None:
        if not re.match(HEX_REGEX, self.background_color):
            raise NotValidColor("Not a valid background color")

        if not re.match(HEX_REGEX, self.font_color):
            raise NotValidColor("Not a valid font color")

    def execute(self) -> None:
        self._validate()
        self._create_folder()
        self._create_config()
