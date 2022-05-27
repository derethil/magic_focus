from enum import Enum
import sys
from i3ipc import Connection, Con


class Direction(Enum):
    UP = "up"
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"


def get_direction() -> Direction:
    if len(sys.argv) < 2:
        raise Exception(f"No Direction found: {sys.argv}")

    return Direction(sys.argv[1])


def main():
    direction = get_direction()
    i3 = Connection()

    curr_window: Con = i3.get_tree().find_focused()

    if "on" in curr_window.floating:
        i3.command(f"workspace back_and_forth")

    else:
        i3.command(f"focus {direction.value}")


if __name__ == "__main__":
    main()
