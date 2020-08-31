from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import pyperclip

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    price = WebDriverWait(browser, 20).until(
                EC.text_to_be_present_in_element((By.ID, "price"), "$100")
            )
    button = browser.find_element_by_id("book")
    button.click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    value = browser.find_element_by_id("input_value")
    x = int(value.text)
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button1 = browser.find_element_by_id("solve")
    button1.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    z = alert_text.split(" ")[-1]
    pyperclip.copy(z)
    alert.accept()

finally:
    browser.quit()
