from argparse import Namespace

from ppaste.abstracts import CommandBase


class Templates(CommandBase):
    @staticmethod
    def execute(args: Namespace):
        print(args)
