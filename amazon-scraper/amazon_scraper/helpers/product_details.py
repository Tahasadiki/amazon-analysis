from selectorlib import Extractor
from selectorlib.formatter import Formatter
import requests
import json
import logging
import os

from .formatters import Categories

logging.basicConfig(level=logging.INFO)

def get_headers():
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    headers = {"User-Agent": user_agent}
    return headers

def get_page(url,headers):
    page = None
    try:
        page = requests.get(url,headers=headers)
    except Exception as e:
        logging.error(e)
    return page

def get_product_details(args):
    #instantiate the product extractor
    formatters = Formatter.get_all()
    product_extractor = Extractor.from_yaml_file('amazon_scraper/selectors/product_selectors.yml',formatters=formatters)

    url = args["<product-url>"]
    headers = get_headers()
    page = get_page(url=url,headers=headers)

    #extract product details from HTML
    if page:
        product_details = product_extractor.extract(page.text)

    return product_details