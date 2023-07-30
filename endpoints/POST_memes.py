import allure
import requests
from endpoints.base_endpoint_rules import EndpointMainRules


class PostEnpoints(EndpointMainRules):
    def __init__(self, base_url, auth_token, texts, urls, tag, infos):
        self.result = self.posts(base_url, auth_token, texts, urls, tag, infos)
        self.result_json = self.result.json()
        self.result_url = self.result_json.get('url')
        self.status_code = self.result.status_code
        self.created_item_id = self.result.json()["id"]
        self.created_items = []

    def posts(self, base_url, auth_token, texts, urls, tag, infos):
        m_url = f'{base_url}/meme'
        headers = {
            "Content-Type": "application/json",
            "Authorization": auth_token
        }
        body = {
            "text": texts,
            "url": urls,
            "tags": tag,
            "info": infos
        }
        result = requests.post(m_url, headers=headers, json=body)
        return result

    def url_is_correct(self, url_control='https://media.tenor.com/Kdw0KeHJMogAAAAd/will-you-please-come-home-randy-marsh.gif'):
        with allure.step('Check meme data (URL)'):
            return self.result_url == url_control
