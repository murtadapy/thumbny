from thumbnails_generator.abstracts import CommandBase


class Generate(CommandBase):
    def __init__(self,
                 template_name: str,
                 title: str,
                 output: str) -> None:
        self.template_name = template_name
        self.title = title
        self.output = output

    def execute() -> None:
        ...
