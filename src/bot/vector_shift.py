import json

import requests


class VectorShiftAPI:
    def __init__(self, api_key: str) -> None:
        """
        Initialize the VectorShiftAPI class with the given API key.

        Parameters
        ----------
        api_key : str
            The API key for accessing the VectorShift API.
        """
        self.url = "https://api.vectorshift.ai/api/pipelines/run"
        self.headers = {
            "Api-Key": api_key,
        }

    def get_response(self, user_message: str) -> str:
        """
        Get a response from the VectorShift API based on the user's message.

        Parameters
        ----------
        user_message : str
            The message from the user that needs to be processed by the VectorShift API.

        Returns
        -------
        str
            The response from the VectorShift API. If the API call fails, returns a default error message.
        """
        data = {
            "inputs": json.dumps({"User_Question": user_message}),
            "pipeline_name": "Shoply Chatbot",
            "username": "sapienzarif",
        }
        response = requests.post(self.url, headers=self.headers, data=data)
        response_json = response.json()
        return response_json.get("response", "Sorry, I couldn't process your request.")
