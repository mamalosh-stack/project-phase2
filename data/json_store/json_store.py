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