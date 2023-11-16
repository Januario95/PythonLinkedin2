import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome('C:/Users/a248433/Documents/drivers/chromedriver106.exe',
						  options=options)
driver.maximize_window()

driver.get('https://selenium.dev')
time.sleep(10)

element_id = driver.find_element(By.ID, 'gsc-iw-id1')
print(element_id)

element_name = driver.find_element(By.NAME, 'submit')
print(element_name)

element_xpath = driver.find_element(By.XPATH, "//section[@class = 'hero homepage']/h1[1]")
print(element_xpath)

element_classname = driver.find_element(By.CLASS_NAME, 'selenium-backers')
print(element_classname)
time.sleep(2)

driver.close()
