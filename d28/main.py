from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("http://flipkart.com/apple-iphone-17-pro-deep-blue-256-gb/product-reviews/itm239d0b996d7f0?pid=MOBHFN6YV7GYZHSM&lid=LSTMOBHFN6YV7GYZHSMOB0WBP&marketplace=FLIPKART")
time.sleep(5)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div[style="padding-left: 16px; padding-top: 16px; padding-bottom: 16px;"]')
    )
)
                
review_cards = driver.find_elements(
    By.CSS_SELECTOR,
    'div[style="padding-left: 16px; padding-top: 16px; padding-bottom: 16px;"]'
)

reviews = []

for card in review_cards:
    review = {}
    
    try:
        review["rating"] = card.find_element(
            By.XPATH,
            './/div[contains(@class,"css-146c3p1") and contains(text(),".")]'
        ).text
    except:
        review["rating"] = None

    try:
        review["title"] = card.find_element(
            By.XPATH,
            './/div[contains(text(),"purchase")]'
        ).text
    except:
        review["title"] = None

    try:
        review["comment"] = card.find_element(
            By.CSS_SELECTOR,
            'span.css-1jxf684'
        ).text
    except:
        review["comment"] = None

    try:
        review["customer"] = card.find_element(
            By.XPATH,
            './/div[contains(text(),",")]'
        ).text
    except:
        review["customer"] = None

    try:
        review["verified"] = card.find_element(
            By.XPATH,
            './/div[contains(text(),"Verified Purchase")]'
        ).text
    except:
        review["verified"] = None

    try:
        review["time"] = card.find_element(
            By.XPATH,
            './/div[contains(text(),"ago")]'
        ).text
    except:
        review["time"] = None

    try:
        review["variant"] = card.find_element(
            By.XPATH,
            './/div[contains(text(),"Review for:")]'
        ).text
    except:
        review["variant"] = None

    try:
        review["helpful"] = card.find_element(
            By.XPATH,
            './/div[contains(text(),"Helpful for")]'
        ).text
    except:
        review["helpful"] = None
    
    reviews.append(review)

print(reviews)
