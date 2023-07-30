import pytest

from auth import authorize


@pytest.fixture(scope='session')
def base_url():
    return 'http://167.172.172.115:52355'


@pytest.fixture(scope='session')
def auth_token(base_url):
    asd_token = authorize(base_url)
    return asd_token


@pytest.fixture(scope='session')
def texts(base_url):
    text = 'Will You Please Come Home Randy Marsh GIF'
    return text


@pytest.fixture(scope='session')
def urls(base_url):
    url_s = 'https://media.tenor.com/Kdw0KeHJMogAAAAd/will-you-please-come-home-randy-marsh.gif'
    return url_s


@pytest.fixture(scope='session')
def tag(base_url):
    tag_s = ["Randy Marsh", "SouthPark", "fun"]
    return tag_s


@pytest.fixture(scope='session')
def infos(base_url):
    info_s = {"type": ["gif", "meme"], "objects": ["picture", "text"]}
    return info_s
