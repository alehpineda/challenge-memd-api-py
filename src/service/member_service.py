import json
from urllib import response
import requests

import src.constants as constants

from fastapi import HTTPException

from src.dao.member_dao import retrieve_member_dao, create_primary_member_dao
from src.models.member_model import DependentMember, PrimaryMember


def retrieve_member_service(member_id: int, token: str) -> requests.Response:
    """Service function that retrieves a member

    Args:
        member_id (int): Member Id
        token (str): Bearer token

    Returns:
        requests.Response: HTTP response
    """
    try:
        return retrieve_member_dao(member_id, token)
    except Exception:
        raise


def create_primary_member_service(
    member: PrimaryMember, token: str
) -> requests.Response:
    """Service function that creates a primary member service

    Args:
        member (PrimaryMember): Primary member payload
        token (str): Bearer token

    Returns:
        requests.Response: HTTP post request response
    """
    try:
        # validate external_id
        validate_external_id = _validate_external_id(
            member_id=member.member.external_id, token=token
        )
        # member validation is done in the model
        if validate_external_id:
            # post member request
            response = create_primary_member_dao(member=member, token=token)
            return response
    except Exception:
        raise


def _validate_external_id(member_id: int, token: str) -> bool:
    """Function that validates member external id

    Args:
        member_id (int): External member id
        token (str): Bearer token

    Raises:
        HTTPException: Raises 400 error if id already exists

    Returns:
        bool: Returns True if id does not exists
    """
    try:
        response = retrieve_member_dao(member_id=member_id, token=token)
        json_data = response.json()
        if constants.ERROR in json_data.keys():
            return True
        else:
            raise HTTPException(
                status_code=400,
                detail=f"External ID: {member_id} already exist",
            )
    except HTTPException:
        raise


def create_dependent_member_service(
    primary_member_id: int, dependent_member: DependentMember, token: str
) -> requests.Response:
    try:
        # validate primary member exists
        primary_response = _validate_primary_member(primary_member_id=primary_member_id, token=token)
        if primary_response:
            pass
            # if dependent does not have address, use primary
            # dependent member validation done in model
            # post dependent request
    except Exception:
        raise


def _validate_primary_member(primary_member_id: int, token: str):
    response = retrieve_member_dao(primary_member_id, token)
    json_data = response.json()
    if constants.EXTERNAL_ID in json_data.keys():
        return response
    else:
        raise HTTPException(
                status_code=400,
                detail=f"External ID: {primary_member_id} does not exist",
            )


def _check_dependent_address():
    pass
