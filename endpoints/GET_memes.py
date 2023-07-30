import requests
from endpoints.base_endpoint_rules import EndpointMainRules


class GetEndpoints(EndpointMainRules):
    def __init__(self, base_url, auth_token, meme_id=None, tag_control=None):
        self.result = self.gets(base_url, auth_token, meme_id)
        self.result_text = self.result.text
        self.result_json = self.result.json()
        self.result_json_tag = self.result_json.get('tags')
        self.status_code = self.result.status_code

    def gets(self, base_url, auth_token, meme_id=None):
        if meme_id:
            m_url = f'{base_url}/meme/{meme_id}'
        else:
            m_url = f'{base_url}/meme'
        token = {
            "Authorization": auth_token
        }
        result = requests.get(m_url, headers=token)
        return result

    def tag_is_correct(self, tag_control):
        if 'data' in self.result_json:
            rzlt = self.result_json['data'][0]['tags']
        else:
            rzlt = self.result_json['tags']
        return rzlt
