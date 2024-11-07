import pathlib
import json

def load_config(config_file="config.json"):
    PATH = pathlib.Path().resolve()
    file_path = PATH / 'config' / config_file
    with open(file_path, 'r') as f:
        config_data = json.load(f)
    return config_data