import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nStart Chrome for testing...")
        browser = webdriver.Chrome()
        browser.implicitly_wait(12)
    elif browser_name == "firefox":
        print("\nStart Firefox for testing...")
        browser = webdriver.Firefox()
        browser.implicitly_wait(12)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nQuit browser!")
    browser.quit()
