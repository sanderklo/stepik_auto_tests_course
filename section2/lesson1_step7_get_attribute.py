from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    picture = browser.find_element_by_id("treasure")
    x_element = picture.get_attribute("valuex")
    y = calc(x_element)

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