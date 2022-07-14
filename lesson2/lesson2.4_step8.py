import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_id("input_value").text
    x = int(x_element)
    y = calc(x)
    field = browser.find_element_by_id("answer")
    field.send_keys(y)

    button_submit = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
