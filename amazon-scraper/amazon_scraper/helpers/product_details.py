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

def get_page_details(url,headers,product_extractor):
    product_details = None
    try:
        page = requests.get(url,headers=headers)
        #extract product details from HTML
        product_details = product_extractor.extract(page.text)
    except Exception as e:
        logging.error(e)
    return product_details

def get_urls(file_path):
    list_urls = []

    try:
        with open(file_path,'r') as urls_file:
            list_urls = urls_file.readlines()        
    except Exception as e:
        logging.error(e)

    return list_urls

def get_product_details(param,isFile=False):
    #instantiate the product extractor
    formatters = Formatter.get_all()
    selectors_path = os.path.join(os.path.dirname(__file__),"selectors/product_selectors.yml")
    product_extractor = Extractor.from_yaml_file(selectors_path,formatters=formatters)

    headers = get_headers()
    
    products_details = []
    list_urls = []
    if isFile:
        file_path = param
        list_urls.extend(get_urls(file_path))
    else:
        url = param
        list_urls.append(url)

    for url in list_urls:
            product_details = get_page_details(url,headers,product_extractor)
            products_details.append(product_details)

    return products_details