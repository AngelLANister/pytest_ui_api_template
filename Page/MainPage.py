import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage():
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Очистить экран от баннера")
    def clear_page(self):
        waiter = WebDriverWait(self.__driver, 40)
        waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]')))
        self.__driver.find_element(
            By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]').click()
