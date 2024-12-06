import argparse

from thumbnails_generator.commands import Create


def main() -> None:
    parser = argparse.ArgumentParser()
    subparesers = parser.add_subparsers(dest="command")

    create_parser = subparesers.add_parser("create",
                                           help="Create a new thumbnail")

    create_parser.add_argument('-t', '--title', required=True,
                               help='Title of the thumbnail')

    args = parser.parse_args()

    if args.create:
        Create.execute()


if __name__ == "__main__":
    raise SystemExit(main())
