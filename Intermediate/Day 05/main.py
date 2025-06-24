# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 05

# Simple web scraper using requests and BeautifulSoup
# You may need to install these libraries first:
# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for i in range(len(quotes)):
    print(f'"{quotes[i].text}" - {authors[i].text}')

# Example Output (will vary depending on the website's content):
# "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking." - Albert Einstein
# "It is our choices, Harry, that show what we truly are, far more than our abilities." - J.K. Rowling
# ...and so on 