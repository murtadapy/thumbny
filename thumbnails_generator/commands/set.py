from ppaste.abstracts import CommandBase


class Set(CommandBase):
    @staticmethod
    def execute():
        print("setting")
