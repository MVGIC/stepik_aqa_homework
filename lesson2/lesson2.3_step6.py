import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_trollface = browser.find_element_by_class_name("trollface")
    button_trollface.click()

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value").text
    x = int(x_element)
    y = calc(x)

    field = browser.find_element_by_id("answer")
    field.send_keys(y)
    button_submit = browser.find_element_by_class_name("btn-primary")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
