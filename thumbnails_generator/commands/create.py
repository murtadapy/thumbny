from ppaste.abstracts import CommandBase


class Create(CommandBase):
    @staticmethod
    def execute():
        print("creating")
