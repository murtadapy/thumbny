
from thumbny.base import CommandBase
from thumbny.models import CreateModel


class CreateCommand(CommandBase):
    def __init__(self, model: CreateModel):
        super().__init__(model)

    def execute(self):
        self.tm.create(self.model)
        print(f"{self.model.key} template has been created successfully")
