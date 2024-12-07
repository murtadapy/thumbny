from typing import Tuple

from dataclasses import dataclass

from thumbnails_generator.templates_manager import TemplateManager
from thumbnails_generator.abstracts import CommandBase

from PIL import Image
from PIL import ImageDraw


@dataclass
class Template:
    name: str
    width: str
    height: int
    background_color: Tuple[int]
    font_color: Tuple[int]
    font: str


class Generate(CommandBase):
    def __init__(self,
                 template_name: str,
                 title: str,
                 output: str) -> None:
        self.template_name = template_name
        self.title = title
        self.output = output

        self.template_manager = TemplateManager()

    def _hex_to_rgb(self, hex_color: str) -> Tuple[int]:
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    def _get_filename(self) -> str:
        return self.title.replace(" ", "_")

    def _get_template(self) -> Template:
        template = self.template_manager.get_template_info(self.template_name)

        background_color = template.get("background_color")
        background_color = self._hex_to_rgb(background_color)

        font_color = template.get("font_color")
        font_color = self._hex_to_rgb(font_color)

        return Template(name=template.get("name"),
                        width=template.get("width"),
                        height=template.get("height"),
                        background_color=background_color,
                        font_color=font_color,
                        font=template.get("font"))

    def execute(self) -> None:
        filename = self._get_filename()
        template = self._get_template()

        image = Image.new(mode="RGB",
                          size=(template.width, template.height),
                          color=template.background_color)

        draw = ImageDraw.Draw(image)

        draw.text(xy=(0, 0), text=self.title)

        image.save(f"{filename}.png")
        image.show()

        print("The thumbnail has been created successfully")
