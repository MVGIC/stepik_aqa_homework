import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_journey= browser.find_element_by_class_name("btn-primary")
    button_journey.click()

    confirm = browser.switch_to_alert()
    confirm.accept()

    x_element = browser.find_element_by_id("input_value").text
    x = int(x_element)
    y = calc(x)

    field = browser.find_element_by_class_name("form-control")
    field.send_keys(y)
    button_submit = browser.find_element_by_class_name("btn-primary")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
