from selenium import webdriver
import unittest

class Test_login(unittest.TestCase):
    def test_login1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first:required")
        input1.send_keys("Petr")
        input2 = browser.find_element_by_css_selector(".second:required")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector(".third:required")
        input3.send_keys("pi@mail.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be correct message")

    def test_login2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector(".first:required")
        input1.send_keys("Petr")
        input2 = browser.find_element_by_css_selector(".second:required")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector(".third:required")
        input3.send_keys("pi@mail.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Should be correct message")


if __name__ == "__main__":
    unittest.main()