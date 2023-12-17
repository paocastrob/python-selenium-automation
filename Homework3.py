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


#1. Find the most optimal locators for Create Account on amazon.com (Registration) page elements:
driver.find_element(By.CSS_SELECTOR,'a-icon a-icon-logo')
driver.find_element(By.CSS_SELECTOR,'a-spacing-small')
driver.find_element(By.CSS_SELECTOR,'input#ap_customer_name')
driver.find_element(By.CSS_SELECTOR,'input#ap_email')
driver.find_element(By.CSS_SELECTOR,'input#ap_password')
driver.find_element(By.CSS_SELECTOR,'input#ap_password_check')
driver.find_element(By.CSS_SELECTOR,'input#continue')
driver.find_element(By.CSS_SELECTOR,"#legalTextRow a[href*='condition_of_use?ie=UTF8&nodeId=508088']")
driver.find_element(By.CSS_SELECTOR,"#legalTextRow a[href*='privacy_notice?ie=UTF8&nodeId=468496']")

#2. Create a test case using BDD that opens target.com, clicks on the cart icon and verifies that “Your cart is empty” message is shown:
Feature: Empty cart message on Target.com

Scenario: Verify "Your cart is empty" message
    Given Open Target main page
    When Click on the Cart icon
    Then Verify the message "Your cart is empty"

from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click on the Cart icon')
def Click_on_the_Cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/icons/assets/glyph/Cart.svg#Cart']".click()

@then('Verify the message')
def Verify_the_message(context):
    expected = 'Your cart is empty'
    actual = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading']".text
    assert expected == actual, f'Expected {expected} did not match actual {actual}

#3. Create a test case to verify that logged out user can access Sign In:
Feature: SignIn tests

Scenario: User can open SignIn page
    Given Open Target main page
    When Click Sing In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened

from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLinkMobile']".click()

@when('From right side navigation menu, click Sign In')
def click_sign_in_from_nav(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-createAccount']".click()

@then('Verify Sign In form opened')
def verify_sign_in_opened(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading']".text
    assert expected == actual, f'Expected {expected} did not match actual {actual}