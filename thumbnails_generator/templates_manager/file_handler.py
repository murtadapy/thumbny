from typing import TYPE_CHECKING
from typing import List

import os
import shutil
import json
from dataclasses import asdict

from thumbnails_generator.models import Template
from thumbnails_generator.exceptions import TemplateNotExist

if TYPE_CHECKING:
    from thumbnails_generator.templates_manager import TemplateManager


class FileHandler:
    def __init__(self,
                 template_manager: "TemplateManager",
                 templates_path: str) -> None:
        self.template_manager = template_manager
        self.templates_path = templates_path

    def create_template_structure(self, name: str) -> str:
        template_path = os.path.join(self.templates_path, name)
        os.mkdir(template_path)
        os.mkdir(os.path.join(template_path, "assets"))
        os.mkdir(os.path.join(template_path, "assets", "fonts"))
        return template_path

    def copy_font(self, font_family: str, template_path: str) -> None:
        font_path = os.path.join(template_path, "assets", "fonts", "font.ttf")
        shutil.copyfile(font_family, font_path)
        return font_path

    def save_config(self, template_path: str, config: Template) -> None:
        config_path = os.path.join(template_path, "config.json")
        with open(config_path, "w") as f:
            json.dump(asdict(config), f, indent=4)

    def delete_template(self, name: str) -> None:
        try:
            path = os.path.join(self.templates_path, name)
            shutil.rmtree(path)
        except FileNotFoundError:
            raise TemplateNotExist(f"{name} template does not exist")

    def get_all_templates(self) -> List[str]:
        return [element for element in os.listdir(self.templates_path)
                if os.path.isdir(os.path.join(self.templates_path, element))]

    def get_template_info(self, name: str) -> dict:
        path = os.path.join(self.templates_path, name, "config.json")
        if not os.path.isfile(path):
            raise TemplateNotExist(f"{name} template does not exist")
        with open(path) as f:
            return json.load(f)
