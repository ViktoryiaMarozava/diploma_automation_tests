import requests
import json
from URLs import *
import allure


@allure.feature('Pet Management')
@allure.story('Get Pet')
@allure.severity(allure.severity_level.NORMAL)
def test_get_pet(create_pet):
    with allure.step("Send GET request to retrieve pet with ID 1"):
        response = requests.get(
            url=f"{URL_SWAGGER}{URL_PET}/1",
            headers={"accept": "application/json"}
        )
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200

    with allure.step("Verify the pet ID and name in the response"):
        pet_id = response.json()["id"]
        assert pet_id == 1

        pet_name = response.json()["name"]
        assert pet_name == "Marysia"

    with allure.step("Send GET request to retrieve pet with invalid ID 'abc'"):
        response = requests.get(
            url=f"{URL_SWAGGER}{URL_PET}/abc",
            headers={"accept": "application/json"}
        )
    with allure.step("Verify the response status code is 404"):
        assert response.status_code == 404


@allure.feature('Pet Management')
@allure.story('Add Pet')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_pet():
    payload = {
        "id": 5,
        "category": {
            "id": 0,
            "name": "cat"
        },
        "name": "Liza",
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
    with allure.step("Send POST request to add a new pet"):
        response = requests.post(
            url=f"{URL_SWAGGER}{URL_PET}",
            headers={"accept": "application/json",
                     "Content-Type": "application/json"},
            json=payload
        )
    with allure.step("Verify the pet ID and name in the response"):
        pet_id = response.json()["id"]
        assert pet_id == 5

        pet_name = response.json()["name"]
        assert pet_name == "Liza"

    with allure.step("Send POST request with missing payload"):
        response = requests.post(
            url=f"{URL_SWAGGER}{URL_PET}",
            headers={"accept": "application/json",
                     "Content-Type": "application/json"}
        )
    with allure.step("Verify the response status code is 405"):
        assert response.status_code == 405


@allure.feature('Pet Management')
@allure.story('Delete Pet')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_pet(create_pet):
    with allure.step("Send DELETE request to delete pet with ID 1"):
        response = requests.delete(
            url=f"{URL_SWAGGER}{URL_PET}/1",
            headers={"accept": "application/json"}
        )
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200

    with allure.step("Verify the response message indicates successful deletion"):
        message = response.json()["message"]
        assert message == "1"

    with allure.step("Send GET request to verify pet with ID 1 is deleted"):
        response = requests.get(
            url=f"{URL_SWAGGER}{URL_PET}/1",
            headers={"accept": "application/json"}
        )
    with allure.step("Verify the response status code is 404"):
        assert response.status_code == 404

    with allure.step("Send DELETE request again to verify pet is already deleted"):
        response = requests.delete(
            url=f"{URL_SWAGGER}{URL_PET}/1",
            headers={"accept": "application/json"}
        )
    with allure.step("Verify the response status code is 404"):
        assert response.status_code == 404


@allure.feature('Pet Management')
@allure.story('Update Pet')
@allure.severity(allure.severity_level.CRITICAL)
def test_update_pet(create_pet):
    update_payload = {
        "id": 1,
        "status": "unavailable"
    }

    with allure.step("Send PUT request to update the pet status to 'unavailable'"):
        response = requests.put(
            url=f"{URL_SWAGGER}{URL_PET}",
            headers={"accept": "application/json"},
            json=update_payload
        )
    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200

    with allure.step("Send GET request to verify the updated status"):
        response = requests.get(
            url=f"{URL_SWAGGER}{URL_PET}/1",
            headers={"accept": "application/json"}
        )
    with allure.step("Verify the pet status is 'unavailable'"):
        status = response.json()["status"]
        assert status == "unavailable"

    update_payload = {
        "id": 777
    }

    with allure.step("Send PUT request with invalid pet ID"):
        response = requests.put(
            url=f"{URL_SWAGGER}{URL_PET}",
            headers={"accept": "application/json"},
            json=update_payload
        )
    with allure.step("Verify the response status code is 404"):
        assert response.status_code == 404


@allure.feature("Pet Management")
@allure.story("Check status of pets")
@allure.title("Test to verify pets with status 'available'")
def test_status_pet(create_pet):
    with allure.step("Send GET request to fetch pets with status 'available'"):
        response = requests.get(
            url=f"{URL_SWAGGER}{URL_PET}{URL_STATUS}",
            params={"status": "available"},
            headers={"accept": "application/json"}
        )

    with allure.step("Check response status code is 200"):
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

    with allure.step("Validate all pets have status 'available'"):
        pet_list = response.json()
        for pet in pet_list:
            status = pet["status"]
            assert status == "available", f"Expected pet status 'available' but got {status}"
