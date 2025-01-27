from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://liderwinnica.pl/2024/11/18/polmaraton-na-majorce/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "wp-block-search__input"))
)

input_element = driver.find_element(By.CLASS_NAME, "wp-block-search__input")
input_element.send_keys("lider winnica")
time.sleep(7)
input_element.send_keys(Keys.ENTER)

time.sleep(15)

driver.quit()