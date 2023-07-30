import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def authorize(base_url):
    url = f"{base_url}/authorize"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "name": os.getenv("LOGIN")
    }
    authorize = requests.post(url, headers=headers, data=json.dumps(data)).text
    json_data = json.loads(authorize)
    asd_token_value = json_data["token"]
    return asd_token_value
