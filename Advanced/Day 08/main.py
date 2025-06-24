# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 08

# Asynchronous Web Scraper
# Needs aiohttp and beautifulsoup4:
# pip install aiohttp beautifulsoup4

import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_quotes(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BeautifulSoup(html, 'html.parser')
        
        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")

        for i in range(len(quotes)):
            print(f'"{quotes[i].text}" - {authors[i].text}')

async def main():
    urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/",
    ]
    tasks = [scrape_quotes(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

# Example Output:
# (Scraped quotes from the first two pages of quotes.toscrape.com, order may vary) 