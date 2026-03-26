import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page.MainPage import MainPage
from Page.ChancePage import ChancePage


# def test_search(browser):
#     main_page = MainPage(browser)
#     main_page.clear_page()
#     film_title = main_page.film("Холоп")

#     with allure.step("Проверить, что название фильма соответствует запросу"):
#         assert film_title == "Холоп"


# def test_search_random_film(browser):
#     chance_page = ChancePage(browser)
#     rnd_film = chance_page.get_random_film()
#     main_page = MainPage(browser)
#     film_title = main_page.film(rnd_film)
 
#     with allure.step("Проверить, что случайный фильм соответствует запросу"):
#         assert film_title == rnd_film


# def test_reviews(browser):
#     chance_page = ChancePage(browser)
#     review_text = chance_page.get_review()

#     with allure.step("Проверить, что открываются рецензии зрителей"):
#         assert review_text == "Рецензии зрителей"


# def test_floating_hints(browser):
#     chance_page = ChancePage(browser)
#     hint_text = chance_page.get_hints()

#     with allure.step("Проверить, что отображаются всплывающие подсказки"):
#         assert hint_text == "Возможно, вы искали"


def test_search_invalid_film(browser):
    main_page = MainPage(browser)
    main_page.clear_page()
    error_invalid_name = main_page.invalid_film()

    with allure.step("Проверить, что отображается ошибка при поиске фильма с невалидным названием"):
        assert error_invalid_name == "К сожалению, по вашему запросу ничего не найдено..."
