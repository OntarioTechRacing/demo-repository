"""Mouser API Script.

Swagger Docs: https://api.mouser.com/api/docs/ui/index#.
Docs Docs: https://api.mouser.com/api/docs/V1.
"""

import os

import requests

BASE_URL = "https://api.mouser.com/"

API_VERSION = os.getenv("MOUSER_API_VERSION")
API_KEY = os.getenv("MOUSER_API_KEY")


def search_part(part_number: str) -> dict:
    """Search for a part number on the Mouser API.

    Args:
        part_number: Mouser part number to search for.

    Returns: Dict json of API response, max 50 search results.
    """
    # Prepare URL and params.
    url = f"{BASE_URL}api/v{API_VERSION}/search/partnumber"

    # Prepare headers and POST request data payload.
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    data = {
        "SearchByPartRequest": {
            "mouserPartNumber": part_number,
            "partSearchOptions": "",
        }
    }

    # Make the POST request.
    response = requests.post(
        url, headers=headers, json=data, params={"apiKey": API_KEY}
    )

    # Check if the request was successful.
    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeWarning(f"Failed to fetch data: {response.status_code}")
