from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

PRODUCT_URL = "https://www.amazon.in/dp/B0BDHX8Z63"
MAX_PAGES = 3


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


def get_asin(url):
    import re
    match = re.search(r"/dp/([A-Z0-9]{10})", url)
    return match.group(1) if match else None


def scrape_reviews(product_url, max_pages=3):
    asin = get_asin(product_url)
    if not asin:
        print("Could not find ASIN in URL")
        return []

    driver = create_driver()
    all_reviews = []

    try:
        for page in range(1, max_pages + 1):
            url = (
                f"https://www.amazon.in/product-reviews/{asin}"
                f"?pageNumber={page}&reviewerType=all_reviews"
            )
            print(f"Scraping page {page}")
            driver.get(url)
            time.sleep(3)

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '[data-hook="review"]')
                    )
                )
            except Exception:
                print("No reviews found")
                break

            review_blocks = driver.find_elements(
                By.CSS_SELECTOR, '[data-hook="review"]'
            )
            print(f"Found {len(review_blocks)} reviews")

            for block in review_blocks:
                def get_text(selector):
                    try:
                        return block.find_element(By.CSS_SELECTOR, selector).text.strip()
                    except Exception:
                        return "N/A"

                # Customer name
                name = get_text(".a-profile-name")

                # Star rating  e.g. "4.0 out of 5 stars"
                rating_raw = get_text('[data-hook="review-star-rating"] .a-icon-alt')
                if rating_raw == "N/A":
                    rating_raw = get_text('[data-hook="cmps-review-star-rating"] .a-icon-alt')
                try:
                    rating = float(rating_raw.split()[0])
                except Exception:
                    rating = 0.0

                # Review title
                title = get_text('[data-hook="review-title"]')

                # Review comment / body
                comment = get_text('[data-hook="review-body"]')

                # Tags (e.g. "Verified Purchase")
                tags = []
                try:
                    badge = block.find_element(
                        By.CSS_SELECTOR, '[data-hook="avp-badge"]'
                    ).text.strip()
                    if badge:
                        tags.append(badge)
                except Exception:
                    pass

                # Date
                date = get_text('[data-hook="review-date"]')

                all_reviews.append({
                    "customer_name": name,
                    "rating":        rating,
                    "title":         title,
                    "comment":       comment,
                    "tags":          tags,
                    "date":          date,
                })

    finally:
        driver.quit()

    return all_reviews


def display_reviews(reviews):
    if not reviews:
        print("No reviews scraped")
        return
    print(f"Total reviews: {len(reviews)}")

    for i, r in enumerate(reviews, 1):
        print(f"\nReview {i}")
        print(f"Name: {r['customer_name']}")
        print(f"Rating: {r['rating']}")
        print(f"Title: {r['title']}")
        print(f"Tags: {r['tags']}")
        print(f"Date: {r['date']}")
        print(f"Comment: {r['comment']}")


if __name__ == "__main__":
    reviews = scrape_reviews(PRODUCT_URL, max_pages=MAX_PAGES)
    display_reviews(reviews)