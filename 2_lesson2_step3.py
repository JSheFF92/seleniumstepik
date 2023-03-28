from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


def calc(x, y):
    return str(int(x)+int(y))


try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(By.CSS_SELECTOR, '[id="num1"]')
    x = x_element1.text
    x_element2 = browser.find_element(By.CSS_SELECTOR, '[id="num2"]')
    y = x_element2.text
    end = calc(x, y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(end)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(2)
    button.click()

finally:
    time.sleep(10)
    browser.quit()