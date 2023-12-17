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

driver.get('https://www.target.com/')

#1. Create a test case that will open the Target Circle page https://www.target.com/circle, and verify there are 5 benefit boxes:

Feature: Main page UI tests
  Scenario: Header has correct amount of links
    Given Open target main page
    Then Verify Target Circle header is present
    And Verify header has 5 links

from selenium.webdriver.common.by import By
from behave import given, then

@given('Open target main page')
def Open_target_main_page(context):
  context.driver.get('https://www.target.com')

@then('Verify Target Circle header is present')
def Verify_Target_Circle_header(context):
  context.driver.find_element(By.CSS_SELECTOR, "[href='/circle']".click()

@then('Verify header has 5 links')
def Verify_header_has_5_links(context):
    context.driver.find_element(By.CSS_SELECTOR, "ul[class*='BenefitCard']"
    context.driver.find_element(By.CSS_SELECTOR, "il[class*='BenefitCard']"
    context.driver.find_element(By.CSS_SELECTOR, "il[class*='BenefitCard']"
    context.driver.find_element(By.CSS_SELECTOR, "il[class*='BenefitCard']"
    context.driver.find_element(By.CSS_SELECTOR, "il[class*='BenefitCard']"
    context.driver.find_element(By.CSS_SELECTOR, "il[class*='BenefitCard']"
    assert expected == actual, f'Expected {expected} did not match actual {actual}
    
#2. [If you did not do that in HW3!] Create your own test case to add any Target’s product into the cart, and make sure it’s there (check that your cart has individual cart items OR the total price, up to you!) 

Feature: Adding product to the cart

Scenario: Adding a product to the cart
    Given Open target main page
    When Search for "toys"
    And Add the first search result to the cart
    Then Verify the product is in the cart

@given('Open target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')

@when('Search for "{product}"')
def search_for_product(context, product):
    search_box = context.driver.find_element(By.ID, 'search')
    search_box.send_keys(product)
    search_box.submit()

@when('Add the first search result to the cart')
def add_first_result_to_cart(context):
    first_search_result = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="product-card"]')))
    first_search_result.click()

    add_to_cart_button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, 'addToCartButton')))
    add_to_cart_button.click()
@then('Verify the product is in the cart')
def verify_product_in_cart(context):
    cart_items = WebDriverWait(context.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.cart-item')))
    assert len(cart_items) > 0, "Product not found in the cart"