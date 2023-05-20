from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser.get(link)
  book = browser.find_element(By.ID, "book")
  
  waitprice = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))  #((By.ID, "<От кого ждем>"), "<Что ждем>"))
  book.click()

  x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
  x = x_element.text
  y = calc(x)

  answer = browser.find_element(By.CSS_SELECTOR, "#answer")
  browser.execute_script("return arguments[0].scrollIntoView(true);", answer)  
  answer.click()
  answer.send_keys(y)

  button = browser.find_element(By.ID, "solve")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)    #browser.execute_script("window.scrollBy(0, 100);") проскроллит страницу на 100 пикселей вниз
  button.click()


finally:
    time.sleep(10)
    browser.quit()