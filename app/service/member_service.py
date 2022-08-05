import requests

import constants

from fastapi import HTTPException

from dao.member_dao import (
    retrieve_member_dao,
    create_primary_member_dao,
    create_dependent_member_dao,
)
from models.member_model import DependentMember, PrimaryMember


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
    """Utility function that validates member external id

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
    """Service function that creates a dependent member

    Args:
        primary_member_id (int): Primary member id
        dependent_member (DependentMember): Dependent member model
        token (str): Bearer token

    Returns:
        requests.Response: HTTP post response request
    """
    try:
        # validate primary member exists
        primary_response = _validate_primary_member(
            primary_member_id=primary_member_id, token=token
        )
        # validate dependent external id does not exists
        dependent_id_validation = _validate_external_id(
            dependent_member.member.external_id, token
        )
        # dependent member validation done in model
        if primary_response and dependent_id_validation:
            # if dependent does not have address, use primary
            _update_dependent_address(dependent_member, primary_response)
            # post dependent request
            dependent_response = create_dependent_member_dao(
                primary_member_id, dependent_member, token
            )
            return dependent_response
    except Exception:
        raise


def _validate_primary_member(
    primary_member_id: int, token: str
) -> requests.Response:
    """Utility function that validates if the primary member exists

    Args:
        primary_member_id (int): Primary member id
        token (str): Bearer token

    Raises:
        HTTPException: If primary member does not exists

    Returns:
        requests.Response: HTTP get response request
    """
    response = retrieve_member_dao(primary_member_id, token)
    json_data = response.json()
    if constants.EXTERNAL_ID in json_data.keys():
        return response
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Primary External ID: {primary_member_id} does not exist",
        )


def _update_dependent_address(
    dependent_member: DependentMember, primary_response: requests.Response
) -> None:
    """Utility function that updates the dependant address if empty

    Args:
        dependent_member (DependentMember): Dependent member model
        primary_response (requests.Response): Primary member HTTP response
    """
    if all(
        [
            dependent_member.member.street_1,
            dependent_member.member.city,
            dependent_member.member.state,
            dependent_member.member.zipcode,
        ]
    ):
        pass
    else:
        json_response = primary_response.json()
        dependent_member.member.street_1 = json_response.get("street_1")
        dependent_member.member.street_2 = json_response.get("street_2")
        dependent_member.member.city = json_response.get("city")
        dependent_member.member.state = json_response.get("state")
        dependent_member.member.zipcode = json_response.get("zipcode")
