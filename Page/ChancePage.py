import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChancePage():
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Получение случайного фильма")
    def get_random_film(self):
        waiter = WebDriverWait(self.__driver, 40)
        waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]')))
        self.__driver.find_element(By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]').click()
        self.__driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        waiter = WebDriverWait(self.__driver, 40)
        waiter.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#search')))
        self.__driver.find_element(By.CSS_SELECTOR, '#search').click()
        waiter = WebDriverWait(self.__driver, 40)
        waiter.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div[class="filmName"]')))
