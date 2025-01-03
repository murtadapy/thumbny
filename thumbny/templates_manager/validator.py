from typing import Optional
from typing import TYPE_CHECKING

import os

from thumbny.exceptions import TemplateExist
from thumbny.exceptions import FontNotFound
from thumbny.exceptions import NotValidFontExtension


if TYPE_CHECKING:
    from thumbny.templates_manager import TemplateManager


class Validator:
    def __init__(self,
                 template_manager: "TemplateManager",
                 templates_path: str) -> None:
        self.template_manager = template_manager
        self.templates_path = templates_path

    def validate_tempalate_key(self, name: str) -> None:
        """Validate the template name

        Args:
            name (str): template name

        Raises:
            TemplateExist: raise template exist
        """
        if name in self.template_manager.get_all_templates():
            raise TemplateExist(f"{name} template already exists")

    def validate_font_family(self, font_family: Optional[str]) -> None:
        """validate font family

        Args:
            font_family (Optional[str]): font family path

        Raises:
            FontNotFound: font not found
            NotValidFontExtension: not valid extension
        """
        if font_family:
            if not os.path.isfile(font_family):
                raise FontNotFound("Font not found")

            suffixes = ("ttf", "otf")
            if not font_family.endswith(suffixes):
                raise NotValidFontExtension("Only ttf and otf extension"
                                            "is supported")
