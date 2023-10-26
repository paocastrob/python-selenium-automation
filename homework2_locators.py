from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

orders_button = driver.find_element(By.ID,"nav-orders").click()

sleep(2)

sign_in_header = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
assert sign_in_header.is_displayed(), "Sign in header is not visible"

email_input_field = driver.find_element(By.ID,'ap_email')
assert email_input_field.is_displayed(), "Email input field is not present"

print('Test Passed')