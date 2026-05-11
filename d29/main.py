from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://www.myntra.com/reviews/30141373")
time.sleep(5)

WebDriverWait(driver,10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.user-review-userReviewWrapper')
    )
)

review_divs = driver.find_elements(By.CSS_SELECTOR, 'div.user-review-userReviewWrapper')

reviews = []

for div in review_divs:
    review = {}

    try:
        review["rating"] = div.find_element(By.CLASS_NAME,"user-review-starWrapper").text
    except:
        review["rating"] = None

    try:
        review["text"] = div.find_element(By.CLASS_NAME,"user-review-reviewTextWrapper").text 
    except:
        review["text"] = None

    try:
        review["name"] = div.find_element(By.CSS_SELECTOR,'div.user-review-left span:first-child').text 
    except:
        review["name"] = None

    try:
        review["date"] = div.find_element(By.CSS_SELECTOR,'div.user-review-left span:last-child').text 
    except:
        review["date"] = None

    try:
        review["likes"] = div.find_elements(By.CLASS_NAME,'user-review-thumb')[0].text 
    except:
        review["likes"] = None

    try:
        review["dislikes"] = div.find_elements(By.CLASS_NAME,'user-review-thumb')[1].text 
    except:
        review["dislikes"] = None

    reviews.append(review)

print(reviews)

