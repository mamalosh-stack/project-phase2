import json
from pathlib import Path

def load_data(filename):
    """Load data from a JSON file."""
    file_path = Path(filename)
    if file_path.exists():
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_data(filename, data):
    """Save data to a JSON file."""
    file_path = Path(filename)
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

def get_data_as_string(filename):
    """Get data from a JSON file as a formatted string."""
    data = load_data(filename)
    return json.dumps(data, indent=2)