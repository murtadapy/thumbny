from __future__ import annotations

from typing import List

import os
import sys

from thumbnails_generator.models import Template
from thumbnails_generator.templates_manager.file_handler import FileHandler
from thumbnails_generator.templates_manager.validator import Validator


class TemplateManager:
    def __new__(cls) -> TemplateManager:
        if not hasattr(cls, "_instance"):
            cls._instance = super(TemplateManager, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        self.templates_path = os.path.join(sys.path[0],
                                           "thumbnails_generator",
                                           "templates")

        self.file_handler = FileHandler(self, self.templates_path)
        self.validtor = Validator(self, self.templates_path)

    def create(self,
               *,
               name: str,
               width: str,
               height: str,
               background_color: str,
               font_color: str,
               font_size: str,
               font_family: str) -> None:
        self.validtor.validate_tempalte_name(name)
        self.validtor.validate_font_family(font_family)

        self.file_handler.create_template_dir(self.templates_path)
        template_Path = self.file_handler.create_template_structure(name)
        font_path = self.file_handler.copy_font(font_family, template_Path)

        config = Template(name=name,
                          width=width,
                          height=height,
                          background_color=background_color,
                          font_color=font_color,
                          font_size=font_size,
                          font_family=font_path)

        self.file_handler.save_config(template_Path, config)

    def delete(self, name: str) -> None:
        self.file_handler.delete_template(name)

    def get_all_templates(self) -> List[str]:
        return self.file_handler.get_all_templates()

    def get_template_info(self, name: str) -> dict:
        return self.file_handler.get_template_info(name)
