from enum import Enum


class Color(Enum):
    BLUE = "\033[94m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"


class ColorPrint:
    @staticmethod
    def print_colored(text: str, color: Color, end: str = "\n") -> None:
        print(f"{color.value}{text}\033[0m", end=end)
