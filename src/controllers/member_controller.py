import src.constants as constants

from fastapi import APIRouter, Security
from fastapi.security.api_key import APIKeyHeader
from src.service.member_service import retrieve_member_service


# fastapi routers starting and config
router = APIRouter()

# Bearer token / api key
auth_scheme = APIKeyHeader(name="Authorization")


@router.get("/retrieve/{member_id}", tags=[constants.GET_TAG])
def retrieve_member(member_id: int, token: str = Security(auth_scheme)):
    try:
        response = retrieve_member_service(member_id, token)
        return response.json()
    except Exception as exp:
        return {"General Exception": f"{exp}"}
