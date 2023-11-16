import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome('C:/Users/a248433/Documents/drivers/chromedriver106.exe',
						  options=options)
driver.maximize_window()

driver.get("C:/Users/a248433/Documents/Learning/LinkedIn/Development/Programming/Python/Python Automation and Testing/Exercise Files/CH02/html_code_02.html")
time.sleep(2)
content = driver.find_element(By.CLASS_NAME, 'content')
print("My class element is:")
print(content)
time.sleep(1)
driver.close()
