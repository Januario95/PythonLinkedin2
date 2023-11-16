import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome('C:/Users/a248433/Documents/drivers/chromedriver106.exe',
						  options=options)
driver.maximize_window()


driver.get("C:/Users/a248433/Documents/Learning/LinkedIn/Development/Programming/Python/Python Automation and Testing/Exercise Files/CH02/html_code_02.html")
time.sleep(4)
username = driver.find_element(By.NAME, 'username')
username.send_keys('Januario')
time.sleep(2)
print("My input element is:")
print(username)
driver.close()
