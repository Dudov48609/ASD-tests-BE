from endpoints.DELETE_memes import DeleteEnpoints
from endpoints.GET_memes import GetEndpoints
from endpoints.POST_memes import PostEnpoints
from endpoints.PUT_memes import PutEnpoints
import pytest
import allure


# @pytest.mark.skip
@allure.issue('https://github.com/usr/project/memes/issues/25')
@allure.title('Create a meme')
@allure.feature('Create a meme')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test involves creating 10 memes and conducting some checks afterwards')
@pytest.mark.parametrize('repeat', range(10))
@pytest.mark.parametrize('urls_control',
                         ['https://media.tenor.com/Kdw0KeHJMogAAAAd/will-you-please-come-home-randy-marsh.gif'])
def test_create_a_meme(base_url, auth_token, texts, urls, tag, infos, urls_control, repeat):
    with allure.step('Requesting POST endpoint with data'):
        create_meme = PostEnpoints(base_url, auth_token, texts, urls, tag, infos)
    with allure.step('Checking response status'):
        assert create_meme.is_response_200(), f"Expected status code 200, but got {create_meme.status_code}"
    with allure.step('Check meme data (URL)'):
        assert create_meme.link_is_correct(urls_control), 'Please check your meme data, incl. URL'
    with allure.step('Printing the result'):
        print(create_meme.result_json)


# @pytest.mark.skip
@allure.issue('https://github.com/usr/project/memes/issues/22')
@allure.title('Change a meme')
@allure.feature('Change a meme')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('This test involves changing the memes and conducting some checks afterwards')
@pytest.mark.parametrize('meme_id', [2, 3])
def test_change_a_meme(base_url, auth_token, meme_id):
    with allure.step('Requesting PUT endpoint with new data'):
        change_meme = PutEnpoints(base_url, auth_token, meme_id)
    with allure.step('Checking response status'):
        assert change_meme.is_response_200(), f"Expected status code 200, but got {change_meme.status_code}"
    with allure.step('Requesting GET endpoint with meme_id'):
        get_meme = GetEndpoints(base_url, auth_token, meme_id)
    with allure.step('Comparing result of changing data'):
        assert get_meme.result_json == change_meme.result_json, 'Not all memes have been have been changed'
    with allure.step('Printing the result'):
        print(change_meme.result_json)
    with allure.step('Printing GET response'):
        print(get_meme.result_json)


# @pytest.mark.skip
@allure.issue('https://github.com/usr/project/memes/issues/30')
@allure.title('Get all memes')
@allure.feature('Get memes')
@allure.story('Get all')
@allure.severity(allure.severity_level.MINOR)
@allure.description('This test involves getting all memes and conducting some checks afterwards')
@pytest.mark.parametrize('tag_c', ['fun'])
def test_get_a_meme_without_id(base_url, auth_token, tag_c):
    with allure.step('Requesting GET endpoint with tag_control'):
        get_meme = GetEndpoints(base_url, auth_token, tag_control=tag_c)
    with allure.step('Checking response status'):
        assert get_meme.is_response_200(), f"Expected status code 200, but got {get_meme.status_code}"
    with allure.step('Checking tag'):
        assert tag_c in get_meme.tag_is_correct(tag_c), f"Tag {tag_c} not found in the response"
    with allure.step('Printing the result'):
        print(get_meme.result_text)


# @pytest.mark.skip
@allure.issue('https://github.com/usr/project/memes/issues/99')
@allure.title('Get meme by id')
@allure.feature('Get memes')
@allure.story('Get by id')
@allure.severity(allure.severity_level.BLOCKER)
@allure.description('This test involves getting a meme by its id and conducting some checks afterwards')
@pytest.mark.parametrize('tag_c', ['fun'])
@pytest.mark.parametrize('meme_id', range(4, 8))
def test_get_a_meme_with_id(base_url, auth_token, meme_id, tag_c):
    with allure.step('Requesting GET endpoint with tag_control'):
        get_meme = GetEndpoints(base_url, auth_token, meme_id, tag_control=tag_c)
    with allure.step('Checking response status'):
        assert get_meme.is_response_200(), f"Expected status code 200, but got {get_meme.status_code}"
    with allure.step('Checking tag'):
        assert tag_c in get_meme.tag_is_correct(tag_c), f"Tag {tag_c} not found in the response"
    with allure.step('Printing the result'):
        print(get_meme.result_json)


# @pytest.mark.skip
@allure.issue('https://github.com/usr/project/memes/issues/12')
@allure.title('Delete meme by id')
@allure.feature('Delete memes')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('This test involves getting a meme by its id and conducting some checks afterwards')
@pytest.mark.parametrize('meme_id', range(2, 22))
def test_delete_a_meme(base_url, auth_token, meme_id):
    with allure.step('Requesting DELETE endpoint'):
        delete_meme = DeleteEnpoints(base_url, auth_token, meme_id)
    with allure.step('Skip deleting if id is not in id range'):
        delete_meme.skip_404()
    with allure.step('Checking response status'):
        assert delete_meme.is_response_200(), f"Expected status code 200, but got {delete_meme.status_code}"
    with allure.step('Printing the result'):
        print(delete_meme.result_text)
