import math
import time

from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value").text
    x = int(x_element)
    y = calc(x)

    field = browser.find_element_by_class_name("form-control")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(y)

    check_box = browser.find_element_by_id("robotCheckbox")
    check_box.click()
    radio_button = browser.find_element_by_id("robotsRule")
    radio_button.click()

    button = browser.find_element_by_class_name("btn-primary")
    button.click()

finally:

    time.sleep(10)
    browser.quit()
