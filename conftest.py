import pytest
from selenium import webdriver
import allure


@pytest.fixture(scope="session")
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
