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

driver.get("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
time.sleep(3)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "content_inner")
    )
)

div = driver.find_element(By.ID,"content_inner")

try:
    name = div.find_element(By.TAG_NAME, 'h1').text.strip()
    print(name)
except:
    print("dne")
    
import pandas as pd
df = pd.DataFrame([[name]])
df.to_csv("books.csv",index=False)
