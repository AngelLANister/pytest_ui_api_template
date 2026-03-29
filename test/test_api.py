import os
import allure
import requests
from dotenv import load_dotenv
load_dotenv()


def test_get_film_by_name(api_headers, base_url):
    resp_get_film = requests.get(
        base_url + '/v1.4/movie/search?query="Холоп"',
        headers=api_headers)
    data = resp_get_film.json()
    with allure.step("Проверить, что возвращается валидное название фильма"):
        assert data["docs"][0]["name"] == "Холоп"
    with allure.step("Проверить, что статус код равен 200"):
        assert resp_get_film.status_code == 200


def test_get_film_by_id(api_headers, base_url):
    resp_get_film = requests.get(
        base_url + '/v1.4/movie/1183582',
        headers=api_headers)
    data = resp_get_film.json()
    with allure.step("Проверить, что возвращается валидное название фильма"):
        assert data["name"] == "Холоп"
    with allure.step("Проверить, что статус код равен 200"):
        assert resp_get_film.status_code == 200


def test_get_random_film(api_headers, base_url):
    resp_get_film = requests.get(
        base_url + '/v1.4/movie/random',
        headers=api_headers)
    with allure.step("Проверить, что статус код равен 200"):
        assert resp_get_film.status_code == 200


def test_get_film_by_invalid_id(api_headers, base_url):
    resp_get_film = requests.get(
        base_url + '/v1.4/movie/15000000',
        headers=api_headers)
    with allure.step("Проверить, что статус код равен 404"):
        assert resp_get_film.status_code == 404


def test_get_film_without_authorization(api_headers, base_url):
    resp_get_film = requests.get(
        base_url + '/v1.4/movie/search?query="Холоп"',
        headers=None)
    with allure.step("Проверить, что статус код равен 401"):
        assert resp_get_film.status_code == 401


def test_delete_film(api_headers, base_url):
    resp_get_film = requests.delete(
        base_url + '/v1.4/movie/1183582',
        headers=api_headers)
    with allure.step("Проверить, что статус код равен 400"):
        assert resp_get_film.status_code == 400


def test_get_film_with_invalid_params(api_headers, base_url):
    resp_get_film = requests.get(
        base_url + '/v1.4/movie?page=1&limit=10&year=abc',
        headers=api_headers)
    with allure.step("Проверить, что статус код равен 400"):
        assert resp_get_film.status_code == 400
