from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome("C:/study_pystuff/selenium_stepik/chromedriver.exe") #подставьте свой путь для драйвера, если необходимо.
    browser.get(link)

    button = browser.find_element_by_class_name("trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value1 = calc(int(browser.find_element_by_id("input_value").text))
    field1 = browser.find_element_by_id("answer")
    button2 = browser.find_element_by_css_selector("[type='submit']")
    
    field1.send_keys(value1)
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()