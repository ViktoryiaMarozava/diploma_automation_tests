import pytest
import requests
from URLs import *


@pytest.fixture
def create_pet():
    payload = {
        "id": 1,
        "category": {
            "id": 0,
            "name": "cat"
        },
        "name": "Marysia",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }
    response = requests.post(
        url=f"{URL_SWAGGER}{URL_PET}",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json=payload
    )
    return response.json()
