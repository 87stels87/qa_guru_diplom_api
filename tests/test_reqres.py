import allure
from jsonschema.validators import validate

from data.schemas import get_users, get_user, register, update_user

USER_COUNT_IN_RESULT = 6
USER_EMAIL = 'janet.weaver@reqres.in'
NEW_JOB = "new job"
HEADERS = {"x-api-key": "reqres-free-v1"}


@allure.epic('API-тесты')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'API')
@allure.severity('Critical')
class Test_reqres():

    @allure.story('Отображение списка юзеров')
    @allure.title('Отображение списка юзеров со второй страницы')
    @allure.feature('Количество юзеров на второй странице')
    def test_get_users(self, setup_api_client):
        response = setup_api_client('get', '/api/users?page=2', headers=HEADERS)
        response_json = response.json()
        assert response.status_code == 200
        validate(response_json, schema=get_users)
        assert response_json["per_page"] == USER_COUNT_IN_RESULT
        pass

    @allure.story('Отображение данных у юзера')
    @allure.title('Отображение почты у заданного юзера')
    @allure.feature('Отображение почты у заданного юзера')
    def test_get_email_at_user(self, setup_api_client):
        user_id = "2"
        response = setup_api_client('get', f'/api/users/{user_id}', headers=HEADERS)
        response_json = response.json()
        assert response.status_code == 200
        validate(response_json, schema=get_user)
        assert response_json["data"]["email"] == USER_EMAIL

    @allure.story('Отображение данных у юзера')
    @allure.title('Отображение почты у заданного юзера')
    @allure.feature('Отображение почты у заданного юзера. Негативный кейс.')
    def test_get_email_at_user_negative(self, setup_api_client):
        user_id = "3"
        response = setup_api_client('get', f'/api/users/{user_id}', headers=HEADERS)
        response_json = response.json()
        assert response.status_code == 200
        validate(response_json, schema=get_user)
        assert response_json["data"]["email"] != USER_EMAIL

    @allure.story('Регистрация и восстановление пользователя')
    @allure.title('Регистрация нового пользователя')
    @allure.feature('Регистрация нового пользователя')
    def test_register_user(self, setup_api_client):
        payload = {"email": "eve.holt@reqres.in", "password": "pistol"}
        response = setup_api_client('post', '/api/register', json=payload, headers=HEADERS)
        response_json = response.json()
        assert response.status_code == 200
        validate(response_json, schema=register)
        assert response_json["token"] is not None

    @allure.story('Редактирование пользователя')
    @allure.title('Редактирование поля job у заданного пользователя')
    @allure.feature('Редактирование поля job у заданного пользователя')
    def test_update_user(self, setup_api_client):
        user_id = "2"
        payload = {"name": "morpheus", "job": "new job"}
        response = setup_api_client('put', f'/api/users/{user_id}', json=payload, headers=HEADERS)
        assert response.status_code == 200
        response_json = response.json()
        validate(response_json, schema=update_user)
        assert response_json["job"] == NEW_JOB

    @allure.story('Редактирование пользователя')
    @allure.title('Удаление пользователя')
    @allure.feature('Удаление заданного пользователя')
    def test_delete_user(self, setup_api_client):
        user_id = "2"
        response = setup_api_client('delete', f'/api/users/{user_id}', headers=HEADERS)
        assert response.status_code == 204
