from argparse import Namespace

from ppaste.abstracts import CommandBase


class Generate(CommandBase):
    @staticmethod
    def execute(args: Namespace):
        print(args)
