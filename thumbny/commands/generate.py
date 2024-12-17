from typing import Tuple

from thumbny.base import CommandBase
from thumbny.models import TemplateModel
from thumbny.models import FillerModel


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class GenerateCommand(CommandBase):
    def __init__(self, model: FillerModel) -> None:
        super().__init__()
        self.model = model

    def _hex_to_rgb(self, hex_color: str) -> Tuple[int]:
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    def _get_filename(self) -> str:
        return self.model.name.replace(" ", "_")

    def _get_template(self) -> TemplateModel:
        template = self.tm.get_template_info(self.model.template_key)
        return TemplateModel(**template)

    def execute(self) -> None:
        filename = self._get_filename()
        template = self._get_template()

        image = Image.new(mode="RGB",
                          size=(template.width, template.height),
                          color=template.background_color)

        draw = ImageDraw.Draw(image)

        if template.font_family:
            try:
                font = ImageFont.truetype(template.font_family,
                                          size=template.font_size)
            except OSError:
                print(f"Font wasn't found at {template.font_family}")
        else:
            font = ImageFont.load_default(size=template.font_size)

        text_width = draw.textlength(self.title, font=font)
        text_height = template.font_size

        text_x = (template.width - text_width) / 2
        text_y = (template.height - text_height) / 2

        draw.text(xy=(text_x, text_y),
                  text=self.title,
                  fill=template.font_color,
                  font=font)

        image.save(f"{filename}.png")
        image.show()

        print("The thumbnail has been created successfully")
