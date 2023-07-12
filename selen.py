from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://www.google.com')
elem1 = driver.find_element(By.ID, 'APjFqb')
elem1.send_keys('крутые бобры')
time.sleep(1)
elem2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
elem2.click()


# time.sleep(3)
# driver.close()
