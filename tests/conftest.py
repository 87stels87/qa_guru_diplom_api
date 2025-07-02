import json
import os

import allure
import pytest
import requests
from allure_commons.types import AttachmentType
from curlify import to_curl
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function")
def setup_api_client():
    def inner_setup_api_client(method, url, **kwargs):
        new_url = os.getenv('BASE_URL') + url
        method = method.upper()
        with allure.step(f'Отправляем запрос {method} {new_url}'):
            with requests.Session() as session:
                response = session.request(method=method, url=new_url, **kwargs)
                message = to_curl(response.request)
                if response.status_code != 204:
                    allure.attach(body=message.encode("utf8"), name="Curl", attachment_type=AttachmentType.TEXT,
                                  extension='txt')
                    allure.attach(body=json.dumps(response.json(), indent=4).encode("utf8"),
                                  name="Response JSON", attachment_type=AttachmentType.JSON, extension='json')
                else:
                    print("Нет контента для статуса 204.")
        return response

    return inner_setup_api_client