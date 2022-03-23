from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    inputresult = browser.find_element_by_id("answer")
    inputresult.send_keys(y)

    robokey = browser.find_element_by_id("robotCheckbox")
    robokey.click()

    roborule = browser.find_element_by_id("robotsRule")
    roborule.click()

    button = browser.find_element_by_tag_name("button")
    button.click()




finally:
    time.sleep(20)
    browser.quit()