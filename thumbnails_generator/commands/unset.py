from ppaste.abstracts import CommandBase


class Unset(CommandBase):
    @staticmethod
    def execute():
        print("unsetting")
