import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.parametrize('url', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'])
def test_add_to_basket_button(browser, url):
    browser.get(url)
    time.sleep(30)  # This allows you to visually check the page content in case the text is in a different language.

    # Проверяем, что на странице есть кнопка добавления в корзину
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
