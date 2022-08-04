import requests
import src.constants as constants

from src.models.primary_member_model import PrimaryMember
from fastapi.encoders import jsonable_encoder


def retrieve_member_dao(member_id: int, token: str) -> requests.Response:
    """DAO function that returns a HTTP response from a request

    Args:
        member_id (int): Member Id
        token (str): Bearer token

    Returns:
        requests.Response: HTTP get request response
    """
    try:
        headers = {"Authorization": token}
        url = f"{constants.RETRIEVE_MEMBER_URL}{member_id}"
        response = requests.get(
            url=url,
            headers=headers,
            timeout=constants.TIMEOUT,
        )
        response.raise_for_status()  # Raises http error if any
        return response
    except requests.exceptions.SSLError as exp:
        return {"SSLError": exp}
    except requests.exceptions.Timeout as exp:
        return {"Timeout Exception": exp}
    except requests.exceptions.RequestException as exp:
        return {"Request Exception": exp}
    except Exception as exp:
        return {"General Exception": exp}


def create_primary_member_dao(
    member: PrimaryMember, token: str
) -> requests.Response:
    """DAO function that returns a HTTP response from a request

    Args:
        member_id (int): Member Id
        token (str): Bearer token

    Returns:
        requests.Response: HTTP post resquest response
    """
    try:
        headers = {"Authorization": token}
        url = f"{constants.CREATE_PRIMARY_MEMBER_URL}"
        response = requests.post(
            url=url,
            headers=headers,
            json=jsonable_encoder(member),
            timeout=constants.TIMEOUT,
        )
        response.raise_for_status()  # Raises http error if any
        return response
    except requests.exceptions.SSLError as exp:
        return {"SSLError": exp}
    except requests.exceptions.Timeout as exp:
        return {"Timeout Exception": exp}
    except requests.exceptions.RequestException as exp:
        return {"Request Exception": exp}
    except Exception as exp:
        return {"General Exception": exp}
