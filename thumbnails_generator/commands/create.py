from argparse import Namespace

from ppaste.abstracts import CommandBase


class Create(CommandBase):
    @staticmethod
    def execute(args: Namespace):
        print(args)