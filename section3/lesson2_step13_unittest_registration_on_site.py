import unittest
from selenium import webdriver
import time

class TestRequired(unittest.TestCase):

    def test_registered_first_site(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        input3.send_keys("kkko@gmail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be registred!")

        time.sleep(3)
        browser.quit()


    def test_registered_second_site(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//input[@placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        input3.send_keys("kkko@gmail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be registred!")

        time.sleep(3)
        browser.quit()

if __name__ == "__main__":
    unittest.main()