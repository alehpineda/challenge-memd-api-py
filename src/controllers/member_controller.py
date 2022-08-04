import src.constants as constants

from fastapi import APIRouter, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from src.models.primary_member_model import PrimaryMember
from src.service.member_service import (
    retrieve_member_service,
    create_primary_member_service,
)


# fastapi routers starting and config
router = APIRouter()

# Bearer token / api key
auth_scheme = APIKeyHeader(name="Authorization")


@router.get("/retrieve/{member_id}", tags=[constants.GET_TAG])
def retrieve_member_controller(
    member_id: int, token: str = Security(auth_scheme)
):
    """Retrive member controller

    Args:
        member_id (int): _description_
        token (str, optional): Bearer Token. Defaults to Security(auth_scheme).

    Returns:
        json: Returns json response
    """
    try:
        response = retrieve_member_service(member_id, token)
        return response.json()
    except Exception:
        raise


@router.post("/create", tags=[constants.POST_TAG])
def create_primary_member_controller(
    member: PrimaryMember, token: str = Security(auth_scheme)
):
    try:
        response = create_primary_member_service(member, token)
        return response.json()
    except Exception:
        raise
