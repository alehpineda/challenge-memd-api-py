import requests

import src.constants as constants


def retrieve_member_service(member_id: int, token: str) -> requests.Response:
    try:
        headers = {"Authorization": token}
        response = requests.get(
            f"http://cratebind-challenge-api.com/memd/members/{member_id}",
            headers=headers,
            timeout=30,
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
