import constants

from typing import Dict
from fastapi import APIRouter

router = APIRouter()


@router.get("/", status_code=200, tags=[constants.GET_TAG])
async def healthcheck() -> Dict[str, str]:
    """API healthcheck

    Returns:
        dict: dictionary with message
    """
    return {"Message": "Member API ready to go!"}
