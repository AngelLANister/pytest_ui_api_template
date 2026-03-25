import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
from Page.MainPage import MainPage
from Page.ChancePage import ChancePage


def test_search(browser):
    main_page = MainPage(browser)
    main_page.clear_page()
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="kp_query"]').send_keys("Холоп")
    browser.find_element(
        By.CSS_SELECTOR,
        'svg[class="styles_icon__a6f9D search-form-submit-button__icon"]').click()
    name = browser.find_element(
        By.CSS_SELECTOR, 'div[class="element most_wanted"]')
    info = name.find_element(By.CSS_SELECTOR, 'div[class="info"]')
    film = info.find_element(By.CSS_SELECTOR, 'a[data-type="film"]').text

    with allure.step("Проверить, что название фильма соответствует запросу"):
        assert film == "Холоп"


def test_search_random_film(browser):
    chance_page = ChancePage(browser)
    chance_page.get_random_film()
    film_name = browser.find_element(By.CSS_SELECTOR, 'div[class="filmName"]')
    rnd_film = film_name.find_element(By.TAG_NAME, 'a').text
    browser.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
    browser.find_element(
        By.CSS_SELECTOR, 'input[name="kp_query"]').send_keys(rnd_film)
    browser.find_element(
        By.CSS_SELECTOR, 'button[type="submit"]').click()
    name = browser.find_element(
        By.CSS_SELECTOR, 'div[class="element most_wanted"]')
    info = name.find_element(By.CSS_SELECTOR, 'div[class="info"]')
    film = info.find_element(By.CSS_SELECTOR, 'a[data-type="film"]').text

    with allure.step("Проверить, что случайный фильм соответствует запросу"):
        assert film == rnd_film


def test_reviews(browser):
    chance_page = ChancePage(browser)
    chance_page.get_random_film()
    link_film = browser.find_element(By.CSS_SELECTOR, 'div[class="filmName"]')
    link_film.find_element(By.CSS_SELECTOR, 'a[href]').click()
    waiter = WebDriverWait(browser, 40)
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR,
        'div[class ="styles_reviewCountLight__rjr84 styles_reviewCount__5VEUJ"]')))
    browser.find_element(
        By.CSS_SELECTOR,
        'div[class ="styles_reviewCountLight__rjr84 styles_reviewCount__5VEUJ"]').click()
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'div[class="users-reviews-block styles_root__L_u4M"]')))
    info = browser.find_element(
        By.CSS_SELECTOR, 'div[class="users-reviews-block styles_root__L_u4M"]')
    film = info.find_element(
        By.CSS_SELECTOR, 'a[data-tid="kp-ui.section-title.more-link"]').text

    with allure.step("Проверить, что открываются рецензии зрителей"):
        assert film == "Рецензии зрителей"


def test_floating_hints(browser):
    chance_page = ChancePage(browser)
    chance_page.get_random_film()
    film_name = browser.find_element(By.CSS_SELECTOR, 'div[class="filmName"]')
    film = film_name.find_element(By.TAG_NAME, 'a').text
    for_hint = film[:2]
    browser.get("https://www.kinopoisk.ru/?utm_referrer=www.kinopoisk.ru")
    browser.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]').send_keys(for_hint)
    waiter = WebDriverWait(browser, 40)
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR,
         'h3[class="styles_title__vIZXW kinopoisk-header-suggest-group__title"]')))
    hint_text = browser.find_element(
        By.CSS_SELECTOR,
         'h3[class="styles_title__vIZXW kinopoisk-header-suggest-group__title"]').text

    with allure.step("Проверить, что отображаются всплывающие подсказки"):
        assert hint_text == "Возможно, вы искали"


def test_search_invalid_film(browser):
    main_page = MainPage(browser)
    main_page.clear_page()
    invalid_film = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    browser.find_element(By.CSS_SELECTOR, 'input[name="kp_query"]').send_keys(invalid_film)
    browser.find_element(By.CSS_SELECTOR,
                      'svg[class="styles_icon__a6f9D search-form-submit-button__icon"]').click()
    waiter = WebDriverWait(browser, 40)
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'div[class="search_results_top"]')))
    film = browser.find_element(By.CSS_SELECTOR, 'h2[style="font:100 18px"]').text

    with allure.step("Проверить, что отображается ошибка при поиске фильма с невалидным названием"):
        assert film == "К сожалению, по вашему запросу ничего не найдено..."
