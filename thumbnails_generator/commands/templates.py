from argparse import Namespace

from thumbnails_generator.abstracts import CommandBase


class Templates(CommandBase):
    def __init__(self, args: Namespace) -> None:
        ...

    def execute() -> None:
        ...