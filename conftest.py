import pytest
from selenium import webdriver
import allure
import os
import requests
from dotenv import load_dotenv


@pytest.fixture()
def browser():
    with allure.step("Открыть и настроить браузер"):
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
        yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()


@pytest.fixture(scope = "session")
def api_headers():
    with allure.step("Передать значение токена"):
        token = os.getenv("token")
        return {'Content-Type':
                    'application/json',
                    'x-api-key': token}


@pytest.fixture(scope = "session")
def base_url():
    with allure.step("Подставить базовый URL"):
        return os.getenv("base_url_for_api")
       