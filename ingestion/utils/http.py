import requests

def get(url: str, params: dict = None, headers: dict = None) -> dict:
    """
    Sends a GET request to the specified URL with optional query parameters and headers.

    Args:
        url (str): The URL to send the GET request to.
        params (dict, optional): A dictionary of query parameters to include in the request. Defaults to None.
        headers (dict, optional): A dictionary of HTTP headers to include in the request. Defaults to None.

    Returns:
        dict: The JSON response from the API.
    """
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()