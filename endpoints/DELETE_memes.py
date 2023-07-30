import pytest
import requests
from endpoints.base_endpoint_rules import EndpointMainRules


class DeleteEnpoints(EndpointMainRules):
    def __init__(self, base_url, auth_token, meme_id):
        self.result = self.delete(base_url, auth_token, meme_id)
        self.result_text = self.result.text
        self.status_code = self.result.status_code

    def delete(self, base_url, auth_token, meme_id):
        m_url = f'{base_url}/meme/{meme_id}'
        headers = {
            "Content-Type": "application/json",
            "Authorization": auth_token
        }
        result = requests.delete(m_url, headers=headers)
        return result

    def skip_404(self):
        if self.status_code == 404:
            pytest.skip("Skipping the test as the status code is 404.")
