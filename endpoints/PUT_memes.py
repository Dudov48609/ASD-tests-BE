import requests
from endpoints.base_endpoint_rules import EndpointMainRules


class PutEnpoints(EndpointMainRules):
    def __init__(self, base_url, auth_token, meme_id):
        self.result = self.puts(base_url, auth_token, meme_id)
        self.result_json = self.result.json()
        self.result_url = self.result_json.get('url')
        self.status_code = self.result.status_code

    def puts(self, base_url, auth_token, meme_id):
        m_url = f'{base_url}/meme/{meme_id}'
        headers = {
            "Content-Type": "application/json",
            "Authorization": auth_token
        }
        body = {
            "id": meme_id,
            "text": 6,
            "url": 'urls_control',
            "tags": [],
            "info": {"type": ["giffffff", "meme"], "objects": ["pictureeeee", "text"]}
        }
        result = requests.put(m_url, headers=headers, json=body)
        return result
