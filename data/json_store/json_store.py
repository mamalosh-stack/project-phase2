import json
from pathlib import Path

users_file = Path("users.json")
appt_file = Path("appointments.json")
inventory_file = Path("inventory.json")


def load_data(path):
    if path.exists():
        with open(path, "r") as f:
            return json.load(f)
    return []


def save_data(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def load_data(json_path):
    path = Path(json_path)

    if path.exists():
        with open(path, "r") as f:
            return json.load(f)

    return []

def save_data(json_path, data):
    with open(json_path, "w") as f:
        json.dump(data, f, indent=4)

def get_data_as_string(json_path):
    data = load_data(json_path)
    return json.dumps(data, indent=2)