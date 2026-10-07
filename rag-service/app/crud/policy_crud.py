import json
from pathlib import Path

from app.models.policy import Policy


DATA_FILE = Path("data/policies.json")


def _load_policies() -> list[dict]:

    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def _save_policies(policies: list[dict]):

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(policies, file, indent=4)


def create_policy(policy_name: str, content: str):

    policies = _load_policies()

    new_id = max(
        [policy["id"] for policy in policies],
        default=0
    ) + 1

    policy = {
        "id": new_id,
        "policy_name": policy_name,
        "content": content
    }

    policies.append(policy)

    _save_policies(policies)

    return policy


def get_policies():

    return _load_policies()


def get_policy(policy_id: int):

    policies = _load_policies()

    for policy in policies:
        if policy["id"] == policy_id:
            return policy

    return None


def update_policy(
    policy_id: int,
    policy_name: str,
    content: str
):

    policies = _load_policies()

    for policy in policies:

        if policy["id"] == policy_id:

            policy["policy_name"] = policy_name
            policy["content"] = content

            _save_policies(policies)

            return policy

    return None


def delete_policy(policy_id: int):

    policies = _load_policies()

    for policy in policies:

        if policy["id"] == policy_id:

            policies.remove(policy)

            _save_policies(policies)

            return True

    return False