import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/adu/development/selenium/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fName = driver.find_element("name", "fName")
fName.send_keys("john")
fName.send_keys()

lName = driver.find_element("name", "lName")
lName.send_keys("doe")

email = driver.find_element("name", "email")
email.send_keys("john.doe@example.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

driver.close()
