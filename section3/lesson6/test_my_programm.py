import time, math, pytest
from selenium import webdriver

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


def answer():
    return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nStart browser for testing...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(12)
    yield browser
    print("\nQuit browser!")
    browser.quit()

@pytest.mark.parametrize('link', links)
def test_correct_answor(browser, link):
    browser.get(link)

    answ = browser.find_element_by_css_selector(".textarea.ember-text-area.ember-view")
    answ.send_keys(str(answer()))

    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    word = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    if "Correct!" != word:
        print(f"===================\n{word}\n===================")
    assert "Correct!" in word, f"Answer must be 'Correct!' in {link}"
