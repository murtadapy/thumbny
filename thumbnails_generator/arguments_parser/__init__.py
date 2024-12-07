import argparse
from argparse import ArgumentParser as AP
from argparse import _SubParsersAction
from argparse import Namespace

from thumbnails_generator.commands import Create
from thumbnails_generator.commands import Delete
from thumbnails_generator.commands import Generate
from thumbnails_generator.commands import Info
from thumbnails_generator.commands import Templates


COMMANDS = {"create": Create,
            "delete": Delete,
            "generate": Generate,
            "info": Info,
            "templates": Templates,
            }


class Parser:
    def _get_create_parser(self, subparser: _SubParsersAction) -> None:
        parser: AP = subparser.add_parser("create",
                                          help="Create a new template")

        parser.add_argument("-n", "--name",
                            required=True,
                            help="Name of the template")

        parser.add_argument("--width",
                            default=1280,
                            help="Width of template")

        parser.add_argument("--height",
                            default=720,
                            help="Height of template")

        parser.add_argument("--background-color",
                            default="#FFFFFF",
                            help="Background color e.g. #FFFFFF")

        parser.add_argument("--font-color",
                            default="#000000",
                            help="Font color e.g. #000000")

        parser.add_argument("--font_path",
                            default="",
                            help="Path to ttf file")

    def _get_delete_parser(self, subparser: _SubParsersAction) -> None:
        parser: AP = subparser.add_parser("delete",
                                          help="Delete a template")

        parser.add_argument("--name",
                            required=True,
                            help="Template name")

    def _get_generate_parser(self, subparser: _SubParsersAction) -> None:
        parser: AP = subparser.add_parser("generate",
                                          help="Generate a thumbnail")

        parser.add_argument("--template-name",
                            required=True,
                            help="Thumbnail template name")

        parser.add_argument("--title",
                            required=True,
                            help="Thumbnail title")

        parser.add_argument("--output",
                            default="",
                            help="Output path")

    def _get_info_parser(self, subparser: _SubParsersAction) -> None:
        parser: AP = subparser.add_parser("info", help="Info of a template")

        parser.add_argument("--name",
                            required=True,
                            help="Template name")

    def _get_templates_parser(self, subparser: _SubParsersAction) -> None:
        subparser.add_parser("templates", help="List all templates")

    def _execute(self, args: Namespace) -> None:
        command_ref = COMMANDS.get(args.command)
        arguments = dict(args._get_kwargs())
        arguments.pop("command")
        command = command_ref(**arguments)
        command.execute()

    def parse(self) -> None:
        parser = argparse.ArgumentParser()
        subparser = parser.add_subparsers(dest="command", required=True)
        self._get_create_parser(subparser)
        self._get_delete_parser(subparser)
        self._get_generate_parser(subparser)
        self._get_info_parser(subparser)
        self._get_templates_parser(subparser)
        args = parser.parse_args()
        self._execute(args)
