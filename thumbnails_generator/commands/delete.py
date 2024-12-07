from argparse import Namespace

from ppaste.abstracts import CommandBase


class Delete(CommandBase):
    @staticmethod
    def execute(args: Namespace):
        print(args)
