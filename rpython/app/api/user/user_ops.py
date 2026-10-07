from pathlib import Path
import json

DATA_FILE = Path("data/users.json")


def read_users():
    """Read users from the JSON file."""
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def write_users(users):
    """Write users to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

