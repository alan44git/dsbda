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
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://www.ajio.com/samsung-galaxy-ultra-smart-watch-47mm-lte-sm-l705f/p/4944219770_multi?")
time.sleep(5)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.comp-section.product-rating')
    )
)

rating_section = driver.find_element(By.CSS_SELECTOR, 'div.comp-section.product-rating')

data = {}

try:
    overall_rating = rating_section.find_element(By.CSS_SELECTOR, 'span._1P7MF').text.split()[0]
    data["overall_rating"] = overall_rating
except:
    data["overall_rating"] = None

try:
    customer_count = rating_section.find_element(By.CSS_SELECTOR, 'div._3AxgC').text
    data["customer_count"] = customer_count
except:
    data["customer_count"] = None

try:
    rating_distribution = {}
    rating_list = rating_section.find_element(By.CSS_SELECTOR, 'div._3KKek ul')
    rating_items = rating_list.find_elements(By.CSS_SELECTOR, 'li')
    
    for idx, item in enumerate(rating_items):
        try:
            percentage = item.find_element(By.CSS_SELECTOR, 'span._25HcP._1pkUd._2Fadd, span._25HcP._2Fadd').text
            star_count = 5 - idx
            rating_distribution[f"{star_count}_star"] = percentage
        except:
            pass
    
    data["rating_distribution"] = rating_distribution
except:
    data["rating_distribution"] = None

try:
    customer_opinions = {}
    opinion_section = rating_section.find_element(By.CSS_SELECTOR, 'div.customer-opnion')
    opinion_questions = opinion_section.find_elements(By.CSS_SELECTOR, 'li.xY6l7')
    
    for question_item in opinion_questions:
        try:
            question_text = question_item.find_element(By.CSS_SELECTOR, 'p._2nsGg').text
            opinion_values = {}
            
            opinion_options = question_item.find_elements(By.CSS_SELECTOR, 'li._3Xuzf')
            for option in opinion_options:
                try:
                    opinion_text = option.find_element(By.CSS_SELECTOR, 'span._25HcP._1pkUd._2Fadd, span._25HcP._2Fadd').text
                    opinion_values[opinion_text.split('(')[0].strip()] = opinion_text
                except:
                    pass
            
            customer_opinions[question_text] = opinion_values
        except:
            pass
    
    data["customer_opinions"] = customer_opinions
except:
    data["customer_opinions"] = None

print(data)

driver.quit()
