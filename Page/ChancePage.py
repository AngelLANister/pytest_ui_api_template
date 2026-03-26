import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChancePage():
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("Получение случайного фильма")
    def get_random_film(self):
        with allure.step("Убрать баннер"):
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]')))
            self.__driver.find_element(
                By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]').click()
        with allure.step("Перейти на страницу с выбором случайного фильма"):
            self.__driver.find_element(
                By.CSS_SELECTOR, 'button[type="submit"]').click()
        with allure.step("Нажать на кнопку 'Случайный фильм'"):
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#search')))
            self.__driver.find_element(By.CSS_SELECTOR, '#search').click()
        with allure.step("Получить название случайного фильма"):    
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'div[class="filmName"]')))
            film_name = self.__driver.find_element(By.CSS_SELECTOR, 'div[class="filmName"]')
            rnd_film = film_name.find_element(By.TAG_NAME, 'a').text
        with allure.step("Вернуться на главную страницу"):
            self.__driver.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input[name="kp_query"]')))
        return rnd_film
        
    @allure.step("Открытие страницы с рецензиями зрителей")
    def get_review(self):
        with allure.step("Убрать баннер"):
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]')))
            self.__driver.find_element(
                By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]').click()
        with allure.step("Перейти на страницу с выбором случайного фильма"):
            self.__driver.find_element(
                By.CSS_SELECTOR, 'button[type="submit"]').click()
            waiter = WebDriverWait(self.__driver, 40)
        with allure.step("Нажать на кнопку 'Случайный фильм'"):
            waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#search')))
            self.__driver.find_element(By.CSS_SELECTOR, '#search').click()
        with allure.step("Перейти в карочку фильма"):
            link_film = self.__driver.find_element(By.CSS_SELECTOR, 'div[class="filmName"]')
            link_film.find_element(By.CSS_SELECTOR, 'a[href]').click()
        with allure.step("Нажать на кнопку *рецензий"):
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                'div[class ="styles_reviewCountLight__rjr84 styles_reviewCount__5VEUJ"]')))
            self.__driver.find_element(
                By.CSS_SELECTOR,
                'div[class ="styles_reviewCountLight__rjr84 styles_reviewCount__5VEUJ"]').click()
        with allure.step("Вернуть текст 'Рецензии зрителей'"):
            waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'div[class="users-reviews-block styles_root__L_u4M"]')))
            info = self.__driver.find_element(
                By.CSS_SELECTOR, 'div[class="users-reviews-block styles_root__L_u4M"]')
            review_text = info.find_element(
                By.CSS_SELECTOR, 'a[data-tid="kp-ui.section-title.more-link"]').text
        
        return review_text
    
    @allure.step("Получение всплывающих подсказок")
    def get_hints(self):
        with allure.step("Убрать баннер"):
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]')))
            self.__driver.find_element(
                By.CSS_SELECTOR, 'button[class="styles_root__mwAP6"]').click()
        with allure.step("Перейти на страницу с выбором случайного фильма"):
            self.__driver.find_element(
                By.CSS_SELECTOR, 'button[type="submit"]').click()
        with allure.step("Нажать на кнопку 'Случайный фильм'"):
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#search')))
            self.__driver.find_element(By.CSS_SELECTOR, '#search').click()
        with allure.step("Получить название случайного фильма"):    
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'div[class="filmName"]')))
            film_name = self.__driver.find_element(By.CSS_SELECTOR, 'div[class="filmName"]')
            rnd_film = film_name.find_element(By.TAG_NAME, 'a').text
        with allure.step("Получить первые 2 буквы названия фильма"):
            for_hint = rnd_film[:2]
        with allure.step("Вернуться на главную страницу"):
            self.__driver.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'input[name="kp_query"]')))
        with allure.step("Ввести первые 2 буквы названия фильма"):    
            self.__driver.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]').send_keys(for_hint)
            waiter = WebDriverWait(self.__driver, 40)
            waiter.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                'h3[class="styles_title__vIZXW kinopoisk-header-suggest-group__title"]')))
        with allure.step("Вернуть текст 'Возможно, вы искали'"):
            hint_text = self.__driver.find_element(
                By.CSS_SELECTOR,
                'h3[class="styles_title__vIZXW kinopoisk-header-suggest-group__title"]').text
            
        return hint_text