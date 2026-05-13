from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://pict.edu")
time.sleep(10)

WebDriverWait(driver,10).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, 'testimonial-item')
    )
)

items = driver.find_elements(By.CLASS_NAME, 'testimonial-item')

testimonials = []

for item in items:
    testimonial = {}
    try:
        testimonial["name"] = item.find_element(By.CLASS_NAME, 'testi-name').text.strip()
    except:
        testimonial["name"] = None
        
    try:
        testimonial["text"] = item.find_element(By.CLASS_NAME, 'overflow-testimonial').text.strip()
    except:
        testimonial["text"] = None
    
    testimonials.append(testimonial)

print(testimonials)

df = pd.DataFrame(testimonials)
df.to_csv('testimonials.csv', index=False)

