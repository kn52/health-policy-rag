from fastapi import APIRouter, HTTPException

from app.models.policy import PolicyCreate, PolicyUpdate
from app.crud.policy_crud import (
    create_policy,
    get_policies,
    get_policy,
    update_policy,
    delete_policy
)


router = APIRouter(
    prefix="/policies",
    tags=["Policies"]
)


@router.post("/")
def create(policy: PolicyCreate):

    return create_policy(
        policy.policy_name,
        policy.content
    )


@router.get("/")
def get_all():

    return get_policies()


@router.get("/{policy_id}")
def get_by_id(policy_id: int):

    policy = get_policy(policy_id)

    if policy is None:
        raise HTTPException(
            status_code=404,
            detail="Policy not found"
        )

    return policy


@router.put("/{policy_id}")
def update(
    policy_id: int,
    policy: PolicyUpdate
):

    updated_policy = update_policy(
        policy_id,
        policy.policy_name,
        policy.content
    )

    if updated_policy is None:
        raise HTTPException(
            status_code=404,
            detail="Policy not found"
        )

    return updated_policy


@router.delete("/{policy_id}")
def delete(policy_id: int):

    deleted = delete_policy(policy_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Policy not found"
        )

    return {
        "message": "Policy deleted successfully"
    }