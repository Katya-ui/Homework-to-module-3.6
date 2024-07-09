import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_has_button_add_to_basket(browser):
    browser.get(link)
    elem = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    time.sleep(10)
    assert len(elem) > 0, "button 'add to basket' not found"
