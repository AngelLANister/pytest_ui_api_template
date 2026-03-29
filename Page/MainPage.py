import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


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
    
    @allure.step("Вернуть название фильма в результатах поиска")
    def film(self, film_name: str):
        with allure.step("Очистить поле ввода"):
            self.__driver.find_element(
                By.CSS_SELECTOR, 'input[name="kp_query"]').clear()
        with allure.step("Ввести название фильма в поле поиска"):
            self.__driver.find_element(
                By.CSS_SELECTOR, 'input[name="kp_query"]').send_keys(film_name)
        with allure.step("Нажать кнопку поиска"):
            self.__driver.find_element(
                By.CSS_SELECTOR,
                'svg[class*="submit-button__icon"]').click()
        with allure.step("Получить название искомого фильма"):
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'div[class="element most_wanted"]')))
            name = self.__driver.find_element(
                By.CSS_SELECTOR, 'div[class="element most_wanted"]')
            info = name.find_element(By.CSS_SELECTOR, 'div[class="info"]')
            film_title = info.find_element(By.CSS_SELECTOR, 'a[data-type="film"]').text
      
        return film_title

    @allure.step("Получить пустое значение при вводе невалидного названия фильма")
    def invalid_film(self):
        with allure.step("Получить строку из случайных символов"):
            invalid_film = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        with allure.step("Ввести название фильма из случайных символов"):
            self.__driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]').send_keys(invalid_film)
            self.__driver.find_element(By.CSS_SELECTOR,
                            'svg[class="styles_icon__a6f9D search-form-submit-button__icon"]').click()
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'div[class="search_results_top"]')))
        with allure.step("Вернуть текст ошибки"):
            error_invalid_name = self.__driver.find_element(By.CSS_SELECTOR, 'h2[style="font:100 18px"]').text
        
        return error_invalid_name