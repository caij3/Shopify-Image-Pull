import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

def parse_image_urls(classes, location, source):
    for a in soup.findAll(attrs={'class': classes}):
        name = a.find(location)
        if name not in results:
            results.append(name.get(source))

driver = webdriver.Chrome()
driver.get("https://weiswesternwear.com/collections/wrangler")
results = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
parse_image_urls("full-unstyled-link", "a", "href")

