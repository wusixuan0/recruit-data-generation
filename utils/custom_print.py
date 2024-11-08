import json
from config.config import CONFIG

def custom_print(data=CONFIG, indent=0):
    """
    Custom function to print JSON-like data with arrays on the same line and dictionaries with 2-space indentation.
    """
    if isinstance(data, dict):
        print(" " * indent + "{")
        for i, (key, value) in enumerate(data.items()):
            print(" " * (indent + 2) + f'"{key}": ', end="")
            custom_print(value, indent + 2)
            if i < len(data) - 1:
                print(",")
        print("\n" + " " * indent + "}", end="")

    elif isinstance(data, list):
        print("[", end="")
        for i, item in enumerate(data):
            custom_print(item, indent)
            if i < len(data) - 1:
                print(", ", end="")
        print("]", end="")

    else:
        print(json.dumps(data), end="")
