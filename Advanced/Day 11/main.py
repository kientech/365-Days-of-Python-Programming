# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 11

# Web Scraping with Selenium for Dynamic Websites
# This script requires 'selenium' and a webdriver (e.g., chromedriver).
# pip install selenium
# Download chromedriver: https://chromedriver.chromium.org/downloads

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_dynamic_quotes():
    """
    Scrapes quotes from a dynamic website that loads content with JavaScript.
    """
    # Use webdriver-manager to automatically handle the driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # Target URL (a site that uses JS to load content)
    url = "http://quotes.toscrape.com/js/"
    
    try:
        driver.get(url)
        
        # Wait for the page to load content
        time.sleep(3) # A simple wait, for more complex sites use explicit waits
        
        print(f"Scraping quotes from {url}:\n")
        
        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        
        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text
            print(f'"{text}" - {author}')
            
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Close the browser window
        driver.quit()

# Run the scraper
scrape_dynamic_quotes()

# Example output will be the quotes from the initial page of the JS version of quotes.toscrape.com 