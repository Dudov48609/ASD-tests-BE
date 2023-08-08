from endpoints.DELETE_memes import DeleteEnpoints
from endpoints.GET_memes import GetEndpoints
from endpoints.POST_memes import PostEnpoints
from endpoints.PUT_memes import PutEnpoints
import pytest
import allure
import csv
import os


def save_to_csv(data_list, filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['Data']
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()

        for index, data in enumerate(data_list, start=1):
            writer.writerow({'Data': data})


created_items_ids = []
folder_path = os.path.dirname(__file__)
csv_file_path = os.path.join(folder_path, 'results.csv')


# @pytest.mark.skip
@allure.issue('https://github.com/usr/project/memes/issues/25')
@allure.title('Create a meme')
@allure.feature('Create a meme')
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test involves creating 10 memes and conducting some checks afterwards')
@pytest.mark.parametrize('repeat', range(10))
def test_create_a_meme(base_url, auth_token, texts, urls, tag, infos, repeat):
    with allure.step('Requesting POST endpoint with data'):
        create_meme = PostEnpoints(base_url, auth_token, texts, urls, tag, infos)
        assert create_meme.is_response_200(), f"Expected status code 200, but got {create_meme.status_code}"
    with allure.step('Check meme data (TEXT)'):
        assert create_meme.url_is_correct(), 'Please check your meme data, incl. URL'
    with allure.step('Printing the result'):
        allure.attach(str(create_meme.result_json), name="Response Data", attachment_type=allure.attachment_type.JSON)
        response_id = create_meme.result_json.get("id")
        allure.attach(str(response_id), name="Response ID", attachment_type=allure.attachment_type.TEXT)
        created_items_ids.append(create_meme.created_item_id)
        save_to_csv(created_items_ids, csv_file_path)
        allure.attach(str(created_items_ids), name="Created items ID", attachment_type=allure.attachment_type.JSON)


def read_csv_and_skip_first_row(filename):
    data_list = []

    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        if csv.Sniffer().has_header(csvfile.read(1024)):
            next(reader)  # Skip the header row if it exists

        for row in reader:
            data = row[0]  # Get the 'Data' column value
            data_list.append(int(data))

    return data_list


data_list = read_csv_and_skip_first_row(csv_file_path)


# @pytest.mark.skip
@allure.issue('https://github.com/usr/project/memes/issues/22')
@allure.title('Change a meme')
@allure.feature('Change a meme')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('This test involves changing the memes and conducting some checks afterwards')
@pytest.mark.parametrize('meme_id', data_list)
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
        allure.attach(str(change_meme.result_json), name="Response Data", attachment_type=allure.attachment_type.JSON)
    with allure.step('Printing GET response'):
        allure.attach(str(get_meme.result_json), name="Response Data", attachment_type=allure.attachment_type.JSON)


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
        get_meme = GetEndpoints(base_url, auth_token)
    with allure.step('Checking response status'):
        assert get_meme.is_response_200(), f"Expected status code 200, but got {get_meme.status_code}"
    with allure.step('Checking tag'):
        assert tag_c in get_meme.tag_is_correct(), f"Tag {tag_c} not found in the response"
    with allure.step('Printing the result'):
        allure.attach(str(get_meme.result_json), name="Response Data", attachment_type=allure.attachment_type.JSON)


# @pytest.mark.skip
@allure.issue('https://github.com/usr/project/memes/issues/99')
@allure.title('Get meme by id')
@allure.feature('Get memes')
@allure.story('Get by id')
@allure.severity(allure.severity_level.BLOCKER)
@allure.description('This test involves getting a meme by its id and conducting some checks afterwards')
@pytest.mark.parametrize('tag_c', ['fun'])
@pytest.mark.parametrize('meme_id', data_list)
def test_get_a_meme_with_id(base_url, auth_token, meme_id, tag_c):
    for meme_id in created_items_ids:
        with allure.step('Requesting GET endpoint with tag_control'):
            get_meme = GetEndpoints(base_url, auth_token, meme_id)
        with allure.step('Checking response status'):
            assert get_meme.is_response_200(), f"Expected status code 200, but got {get_meme.status_code}"
        with allure.step('Checking tag'):
            assert tag_c in get_meme.tag_is_correct(), f"Tag {tag_c} not found in the response"
        with allure.step('Printing the result'):
            allure.attach(str(get_meme.result_json), name="Response Data", attachment_type=allure.attachment_type.JSON)


# @pytest.mark.skip
@allure.issue('https://github.com/usr/project/memes/issues/12')
@allure.title('Delete meme by id')
@allure.feature('Delete memes')
@allure.severity(allure.severity_level.NORMAL)
@allure.description('This test involves getting a meme by its id and conducting some checks afterwards')
@pytest.mark.parametrize('meme_id', data_list)
def test_delete_a_meme(base_url, auth_token, meme_id):
    with allure.step('Requesting DELETE endpoint'):
        delete_meme = DeleteEnpoints(base_url, auth_token, meme_id)
    with allure.step('Checking response status'):
        assert delete_meme.is_response_200(), f"Expected status code 200, but got {delete_meme.status_code}"
