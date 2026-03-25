import os
import allure
import requests
from dotenv import load_dotenv
load_dotenv()


def test_get_film_by_name():
    token = os.getenv('token')
    base_url_for_api = os.getenv('base_url_for_api')
    params = {
        'page': 1,
        'limit': 1,
    }
    headers_auth = {'Content-Type':
                    'application/json',
                    'x-api-key': token}
    resp_get_film = requests.get(
        base_url_for_api + '/v1.4/movie/search?query="Холоп"',
        headers=headers_auth, params=params)
    data = resp_get_film.json()
    with allure.step("Проверить, что возвращается валидное название фильма"):
        assert data["docs"][0]["name"] == "Холоп"
    with allure.step("Проверить, что статус код равен 200"):
        assert resp_get_film.status_code == 200


def test_get_film_by_id():
    token = os.getenv('token')
    base_url_for_api = os.getenv('base_url_for_api')
    headers_auth = {'Content-Type':
                    'application/json',
                    'x-api-key': token}
    resp_get_film = requests.get(
        base_url_for_api + '/v1.4/movie/1183582',
        headers=headers_auth)
    data = resp_get_film.json()
    with allure.step("Проверить, что возвращается валидное название фильма"):
        assert data["name"] == "Холоп"
    with allure.step("Проверить, что статус код равен 200"):
        assert resp_get_film.status_code == 200


def test_get_random_film():
    token = os.getenv('token')
    base_url_for_api = os.getenv('base_url_for_api')
    params = {
        'page': 1,
        'limit': 1,
    }
    headers_auth = {'Content-Type':
                    'application/json',
                    'x-api-key': token}
    resp_get_film = requests.get(
        base_url_for_api + '/v1.4/movie/random',
        headers=headers_auth, params=params)
    with allure.step("Проверить, что статус код равен 200"):
        assert resp_get_film.status_code == 200


def test_get_film_by_invalid_id():
    token = os.getenv('token')
    base_url_for_api = os.getenv('base_url_for_api')
    params = {
        'page': 1,
        'limit': 1,
    }
    headers_auth = {'Content-Type':
                    'application/json',
                    'x-api-key': token}
    resp_get_film = requests.get(
        base_url_for_api + '/v1.4/movie/15000000',
        headers=headers_auth, params=params)
    with allure.step("Проверить, что статус код равен 404"):
        assert resp_get_film.status_code == 404


def test_get_film_without_authorization():
    base_url_for_api = os.getenv('base_url_for_api')
    params = {
        'page': 1,
        'limit': 1,
    }
    headers_auth = {'Content-Type':
                    'application/json',
                    'x-api-key': None}
    resp_get_film = requests.get(
        base_url_for_api + '/v1.4/movie/search?query="Холоп"',
        headers=headers_auth, params=params)
    with allure.step("Проверить, что статус код равен 401"):
        assert resp_get_film.status_code == 401


def test_delete_film():
    token = os.getenv('token')
    base_url_for_api = os.getenv('base_url_for_api')
    headers_auth = {'Content-Type':
                    'application/json',
                    'x-api-key': token}
    resp_get_film = requests.delete(
        base_url_for_api + '/v1.4/movie/1183582',
        headers=headers_auth)
    with allure.step("Проверить, что статус код равен 400"):
        assert resp_get_film.status_code == 400


def test_get_film_with_invalid_params():
    token = os.getenv('token')
    base_url_for_api = os.getenv('base_url_for_api')
    params = {
        'page': 1,
        'limit': 1,
    }
    headers_auth = {'Content-Type':
                    'application/json',
                    'x-api-key': token}
    resp_get_film = requests.get(
        base_url_for_api + '/v1.4/movie?page=1&limit=10&year=abc',
        headers=headers_auth, params=params)
    with allure.step("Проверить, что статус код равен 400"):
        assert resp_get_film.status_code == 400
