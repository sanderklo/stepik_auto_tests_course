from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_tag_name("button")
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    inputresult = browser.find_element_by_id("answer")
    inputresult.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()


finally:
    time.sleep(20)
    browser.quit()