from selenium import webdriver
from selenium.webdriver.common.by import By


def initiate_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    
    driver = webdriver.Chrome('C:/Users/a248433/Documents/drivers/chromedriver106.exe',
                    options=options)
    driver.maximize_window()
    return driver

driver = initiate_driver()

driver.get("C:/Users/a248433/Documents/Learning/LinkedIn/Development/Programming/Python/Python Automation and Testing/Exercise Files/CH02/html_code_02.html")
login_form = driver.find_element(By.ID, 'loginForm')
print("My login form element is:")
print(login_form)
driver.close()
