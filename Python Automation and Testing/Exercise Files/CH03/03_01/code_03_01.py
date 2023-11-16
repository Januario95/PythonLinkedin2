from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome('C:/Users/a248433/Documents/drivers/chromedriver106.exe',
						  options=options)
driver.maximize_window()

driver = webdriver.Firefox()
driver.get("http://python.org");
time.sleep(5)

search = driver.find_element(By.NAME, 'q');
search.clear();
search.send_keys("pycon");
search.send_keys(Keys.RETURN);
time.sleep(4)

driver.close();
