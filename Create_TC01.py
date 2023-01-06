from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://en-gb.facebook.com/reg/")
time.sleep(3)
driver.find_element(By.NAME,"firstname").send_keys("Joko")
driver.find_element(By.NAME,"lastname").send_keys("Setiono")
driver.find_element(By.NAME,"reg_email__").send_keys("089624866262")
driver.find_element(By.ID,"password_step_input").send_keys("QA2023")
dropDown =  Select(driver.find_element(By.NAME, "birthday_day")).select_by_index(9)
dropDown =  Select(driver.find_element(By.NAME, "birthday_month")).select_by_value("4")
dropDown =  Select(driver.find_element(By.NAME, "birthday_year")).select_by_value("1996")
radio    = driver.find_element(By.XPATH,"//label[text()='Male']").click()
btn      = driver.find_element(By.NAME,"websubmit").click()
time.sleep(10)
