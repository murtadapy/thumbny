from __future__ import annotations

from typing import List

import os
import sys
import json
import shutil

from thumbnails_generator.exceptions import TemplateExist
from thumbnails_generator.exceptions import TemplateNotExist
from thumbnails_generator.exceptions import FontNotFound
from thumbnails_generator.exceptions import FontExtensionError


class TemplateManager:
    def __new__(cls) -> TemplateManager:
        if not hasattr(cls, "_instance"):
            cls._instance = super(TemplateManager, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.templates_path = os.path.join(sys.path[0],
                                           "thumbnails_generator",
                                           "templates")

    def create(self,
               *,
               name: str,
               width: str,
               height: str,
               background_color: str,
               font_color: str,
               font_path: str) -> None:

        if name in self.get_all_templates():
            raise TemplateExist(f"{name} template is already exist")

        if font_path and not os.path.isfile(font_path):
            raise FontNotFound("Font is not found")

        if font_path and not font_path.endswith("ttf"):
            raise FontExtensionError("Only ttf extension is supported")

        template_path = os.path.join(self.templates_path, name)
        os.mkdir(template_path)

        config = {
            "name": name,
            "width": width,
            "height": height,
            "background_color": background_color,
            "font_color": font_color,
            "font_path": font_path
        }

        config_path = os.path.join(template_path, "config.json")
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)

    def delete(self, name: str) -> None:
        try:
            path = os.path.join(self.templates_path, name)
            shutil.rmtree(path)
        except FileNotFoundError:
            raise TemplateNotExist(f"{name} template is not exist")

    def get_all_templates(self) -> List[str]:
        templates = []
        for element in os.listdir(self.templates_path):
            if os.path.isdir(os.path.join(self.templates_path, element)):
                templates.append(element)
        return templates

    def get_template_info(self, name: str) -> dict:
        path = os.path.join(self.templates_path, name, "config.json")

        if not os.path.isfile(path):
            raise TemplateNotExist(f"{name} template is not exist")

        with open(path) as f:
            details = json.load(f)

        return details
