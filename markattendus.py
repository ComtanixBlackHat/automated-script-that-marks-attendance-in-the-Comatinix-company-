from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from lxml import html
import re


global driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://pm.comtanix.com/index.php/signin")


driver.find_element(By.ID, 'email').send_keys('email@c.com')
driver.find_element(By.ID, 'password').send_keys('yourpass')
driver.find_element(By.XPATH, '//*[@id="signin-form"]/button').submit()
print (driver.current_url)

driver.get(driver.current_url)
# timecard-clock-out

driver.find_element(By.XPATH, '//*[@id="js-clock-in-out"]/div/div[2]').click()



