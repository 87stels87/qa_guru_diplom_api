import json

import allure
from allure_commons.types import AttachmentType
from curlify import to_curl
from jsonschema.validators import validate
from requests import sessions

from data.schemas import get_users, get_user, register, update_user


def setup_api_client(method, url, **kwargs):
    args = kwargs
    base_url = "https://reqres.in"
    new_url = base_url + url
    method = method.upper()
    with allure.step(f'Отправляем запрос {method} {url}  {args if len(args) != 0 else ""} '):
        with sessions.Session() as session:
            response = session.request(method=method, url=new_url, **kwargs)
            message = to_curl(response.request)
            if response.status_code != 204:
                allure.attach(body=message.encode("utf8"), name="Curl", attachment_type=AttachmentType.TEXT,
                              extension='txt')
                allure.attach(body=json.dumps(response.json(), indent=4).encode("utf8"), name="Response Json",
                              attachment_type=AttachmentType.JSON, extension='json')
            else:
                print("Нет контента для статуса 204.")
    return response


user_count_in_result = 6
user_email = 'janet.weaver@reqres.in'
new_job = "new job"
headers = {"x-api-key": "reqres-free-v1"}


@allure.epic('API-тесты')
@allure.story('Отображение списка юзеров')
@allure.title('Отображение списка юзеров со второй страницы')
@allure.feature('Количество юзеров на второй странице')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'API')
@allure.severity('Critical')
def test_get_users():
    response = setup_api_client('get', '/api/users?page=2', headers=headers)
    response_json = response.json()
    assert response.status_code == 200
    validate(response_json, schema=get_users)
    assert response_json["per_page"] == user_count_in_result


@allure.epic('API-тесты')
@allure.story('Отображение данных у юзера')
@allure.title('Отображение почты у заданного юзера')
@allure.feature('Отображение почты у заданного юзера')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'API')
@allure.severity('Critical')
def test_get_email_at_user(user_id="2"):
    response = setup_api_client('get', f'/api/users/{user_id}', headers=headers)
    response_json = response.json()
    assert response.status_code == 200
    validate(response_json, schema=get_user)
    assert response_json["data"]["email"] == user_email


@allure.epic('API-тесты')
@allure.story('Отображение данных у юзера')
@allure.title('Отображение почты у заданного юзера')
@allure.feature('Отображение почты у заданного юзера. Негативный кейс.')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'API')
@allure.severity('Critical')
def test_get_email_at_user_negative(user_id="3"):
    response = setup_api_client('get', f'/api/users/{user_id}', headers=headers)
    response_json = response.json()
    assert response.status_code == 200
    validate(response_json, schema=get_user)
    assert response_json["data"]["email"] != user_email


@allure.epic('API-тесты')
@allure.story('Регистрация и восстановление пользователя')
@allure.title('Регистрация нового пользователя')
@allure.feature('Регистрация нового пользователя')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'API')
@allure.severity('Critical')
def test_register_user():
    payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = setup_api_client('post', '/api/register', json=payload, headers=headers)
    response_json = response.json()
    assert response.status_code == 200
    validate(response_json, schema=register)
    assert response_json["token"] is not None


@allure.epic('API-тесты')
@allure.story('Редактирование пользователя')
@allure.title('Редактирование поля job у заданного пользователя')
@allure.feature('Редактирование поля job у заданного пользователя')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'API')
@allure.severity('Critical')
def test_update_user(user_id="2"):
    payload = {"name": "morpheus", "job": "new job"}
    response = setup_api_client('put', f'/api/users/{user_id}', json=payload, headers=headers)
    assert response.status_code == 200
    response_json = response.json()
    validate(response_json, schema=update_user)
    assert response_json["job"] == new_job


@allure.epic('API-тесты')
@allure.story('Редактирование пользователя')
@allure.title('Удаление пользователя')
@allure.feature('Удаление заданного пользователя')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'API')
@allure.severity('Critical')
def test_delete_user(user_id="2"):
    response = setup_api_client('delete', f'/api/users/{user_id}', headers=headers)
    assert response.status_code == 204
