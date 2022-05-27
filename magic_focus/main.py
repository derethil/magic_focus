from i3ipc import Connection, Con
from argparse import ArgumentParser, Namespace


def handle_args() -> Namespace:
    parser = ArgumentParser(
        prog="magic_focus",
        description="Handle i3 focusing between floating and tiling windows.",
    )

    parser.add_argument(
        "direction",
        choices=["up", "down", "left", "right"],
        help="Direction to focus",
    )

    return parser.parse_args()


def main():
    args = handle_args()
    i3 = Connection()

    curr_window: Con = i3.get_tree().find_focused()

    if "on" in curr_window.floating:
        i3.command(f"workspace back_and_forth")

    else:
        i3.command(f"focus {args.direction}")


if __name__ == "__main__":
    main()
