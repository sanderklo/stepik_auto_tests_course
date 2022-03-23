import time, math, pytest
from selenium import webdriver

link = "https://stepik.org/lesson/236895/step/1"
sentens = []

try:
    print("\nStart browser for testing...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(12)
    browser.get(link)

    answ = browser.find_element_by_css_selector(".textarea.ember-text-area.ember-view")
    answ.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    word = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    if "Correct!" != word:
        sentens.append(word)
    assert "Correct!" in word, f"Answer must be 'Correct!' in {link}"
    

finally:
    time.sleep(40)
    print("\nQuit browser!")
    browser.quit()