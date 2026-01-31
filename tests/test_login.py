from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login():
    driver = webdriver.Chrome()

    # Open login page (example demo site)
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    # Enter username
    driver.find_element(By.ID, "username").send_keys("tomsmith")

    # Enter password
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Click login button
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)

    # Verify login success
    message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in message

    driver.quit()
