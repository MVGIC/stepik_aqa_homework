import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("num1").text
    y_element = browser.find_element_by_id("num2").text
    x = int(x_element)
    y = int(y_element)
    sum = x + y

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))

    button = browser.find_element_by_class_name("btn")
    button.click()

finally:

    time.sleep(10)
    browser.quit()
