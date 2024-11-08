import pathlib
import json
import os

def save_json(data, filename, folder="output"):
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved {filename} to {folder}")

def load_json(config_file="config.json"):
    PATH = pathlib.Path().resolve()
    file_path = PATH / 'config' / config_file
    with open(file_path, 'r') as f:
        config_data = json.load(f)
    return config_data