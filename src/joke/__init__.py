import requests
from typing import Dict, Any

def get_chuck_norris_joke() -> Dict[str, Any]:
    """Make HTTP request to get JSON joke object and return to user

    Returns:
        Dict[str, Any]: JSON object containing the joke
    """
    response = requests.get("https://api.chucknorris.io/jokes/random")

    if response.status_code == 200:
        return response.json()

    raise Exception(f"Can not retrieve joke data status_code={response.status_code}")
