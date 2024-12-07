from typing import Optional
from typing import List

import os
import sys
import json

from thumbnails_generator.abstracts import CommandBase
from thumbnails_generator.exceptions import TemplateExist


class Create(CommandBase):
    def __init__(self,
                 *,
                 name: str,
                 width: Optional[str],
                 height: Optional[str],
                 background: Optional[str],
                 color: Optional[str],
                 font: Optional[str]) -> None:
        self.name = name
        self.width = width
        self.height = height
        self.background = background
        self.color = color
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
            "background": self.background,
            "color": self.color,
            "font": self.font
        }

        path = os.path.join(self.template_path, "config.json")
        with open(path, "w") as f:
            json.dump(config, f, indent=4)

    def execute(self) -> None:
        self._create_folder()
        self._create_config()
