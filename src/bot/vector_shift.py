import json

import requests

from .settings import settings

url = "https://api.vectorshift.ai/api/pipelines/run"

headers = {
    "Api-Key": settings.VECTORSHIFT_API_KEY,
}

question = "Can a business be both a Vendor and Influencer?"

data = {
    # String inputs, or JSON representations of files for File inputs
    "inputs": json.dumps({"User_Question": question}),
    "pipeline_name": "Shoply Chatbot",
    "username": "sapienzarif",
}

response = requests.post(url, headers=headers, data=data)
response = response.json()
print(response)
