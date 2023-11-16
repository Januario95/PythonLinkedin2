import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--incognito')

driver= webdriver.Chrome('C:/Users/a248433/Documents/drivers/chromedriver106.exe',
						 options=options)
driver.maximize_window()

driver.get("C:/Users/a248433/Documents/Learning/LinkedIn/Development/Programming/Python/Python Automation and Testing/Exercise Files/CH02/html_code_02.html")
time.sleep(2)
login_form_absolute = driver.find_element(By.XPATH, "/html/body/form[1]")
login_form_relative = driver.find_element(By.XPATH, "//form[1]")
login_form_id = driver.find_element(By.XPATH, "//form[@id='loginForm']")
time.sleep(1)
print("My login form is:")
print(login_form_absolute)
print(login_form_relative)
print(login_form_id)
time.sleep(1)
driver.close()
