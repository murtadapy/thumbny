import os
import sys
import shutil

from thumbnails_generator.abstracts import CommandBase
from thumbnails_generator.exceptions import TemplateNotExist


class Delete(CommandBase):
    def __init__(self,
                 name: str) -> None:
        self.name = name

    def _delete_folder(self) -> None:
        try:
            path = os.path.join(sys.path[0],
                                "thumbnails_generator",
                                "templates",
                                self.name)
            shutil.rmtree(path)
        except FileNotFoundError:
            raise TemplateNotExist(f"Template {self.name} is not exist")

    def execute(self) -> None:
        self._delete_folder()
