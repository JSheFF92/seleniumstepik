from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, "[id=book]")
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button1.click()


    x_element = browser.find_element(By.CSS_SELECTOR, '[id=input_value]')
    x = x_element.text
    print(x)
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '[id=answer]')
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "[id=solve]")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

