from typing import Tuple
from typing import Optional

from thumbny.base import CommandBase
from thumbny.models import TemplateModel
from thumbny.models import LabelModel
from thumbny.models import FillerModel
from thumbny.enums import PositionTypeEnum
from thumbny.enums import XPositionEnum
from thumbny.enums import YPositionEnum


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class GenerateCommand(CommandBase):
    def __init__(self,
                 model: FillerModel,
                 should_present: bool = False) -> None:
        super().__init__()
        self.model = model
        self.should_present = should_present

    def _hex_to_rgb(self, hex_color: str) -> Tuple[int]:
        """Convert hex to rgb color

        Args:
            hex_color (str): hex color e.g. #FF0000

        Returns:
            Tuple[int]: RGB color
        """
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    def _get_filename(self) -> str:
        """Get file name out of model name

        Returns:
            str: fixed file name
        """
        return self.model.name.replace(" ", "_")

    def _get_template(self) -> TemplateModel:
        """Get template

        Returns:
            TemplateModel: template model object
        """
        template = self.tm.get_template_info(self.model.template_key)
        return TemplateModel.make(template)

    def _get_label(self,
                   template: TemplateModel,
                   label_key: str) -> Optional[LabelModel]:
        """Get label model

        Args:
            template (TemplateModel): template model object
            label_key (str): label key

        Returns:
            Optional[LabelModel]: label model object
        """
        for label in template.labels:
            if label.key == label_key:
                return label
        return None

    def execute(self) -> None:
        """Execute the generate command"""
        filename = self._get_filename()
        template = self._get_template()

        image = Image.new(mode="RGB",
                          size=(template.width, template.height),
                          color=template.background_color)

        draw = ImageDraw.Draw(image)

        if template.background_image:
            background = Image.open(template.background_image)
            image.paste(background, (0, 0))

        for label in self.model.labels:
            label_model = self._get_label(template, label.key)

            if label_model.font_family:
                try:
                    font = ImageFont.truetype(label_model.font_family,
                                              size=label_model.font_size)
                except OSError:
                    print(f"Font wasn't found at {label_model.font_family}")
            else:
                font = ImageFont.load_default(size=label_model.font_size)

            width = draw.textlength(label.value, font=font)
            height = label_model.font_size

            if label_model.position.key == PositionTypeEnum.RELATIVE.value:
                x_positions = {
                    XPositionEnum.LEFT.value: 0,
                    XPositionEnum.CENTER.value: (template.width - width) / 2,
                    XPositionEnum.RIGHT.value: template.width - width
                }

                y_positions = {
                    YPositionEnum.TOP.value: 0,
                    YPositionEnum.CENTER.value: (template.height - height) / 2,
                    YPositionEnum.BOTTOM.value: template.height - height
                }

                x_pos_key, y_pos_key = label_model.position.value.split(",")

                x_padding = 0
                y_padding = 0
                padding = label_model.padding
                if padding:
                    x_padding = padding.left - padding.right
                    y_padding = padding.top - padding.bottom

                x_text = x_positions.get(x_pos_key, 0) + x_padding
                y_text = y_positions.get(y_pos_key, 0) + y_padding

            draw.text(xy=(x_text, y_text),
                      text=label.value,
                      fill=label_model.font_color,
                      font=font)

        image.save(f"{filename}.png")

        if self.should_present:
            image.show()

        print("The thumbnail has been created successfully")
