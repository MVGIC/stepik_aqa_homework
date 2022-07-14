import os
import time

from selenium import webdriver

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname").send_keys("Ivan")
    lastname = browser.find_element_by_name("lastname").send_keys("Ivanov")
    email = browser.find_element_by_name("email").send_keys("testemail@mail.ru")

    button_file = browser.find_element_by_css_selector("input#file")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test_stepik")
    button_file.send_keys(file_path)

    button_submit = browser.find_element_by_class_name("btn-primary")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()

# import os
# print(__file__)
# print(os.path.join(os.path.dirname(__file__), ".."))
# print(os.path.dirname(os.path.realpath(__file__)))
# print(os.path.abspath(os.path.dirname(__file__)))
