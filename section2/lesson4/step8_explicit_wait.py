from pydoc import text
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_id("book")
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    inputresult = browser.find_element_by_id("answer")
    inputresult.send_keys(y)

    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    time.sleep(20)
    browser.quit()