"""
Usage:
    amazon-scraper scrape (--file | --url) <product-url>

Arguments:
    <product-url>   Amazon Product Details URL(s)

Options: 
    --file          Input as a file containing a list of Amazon URLs              
    --url           Input as a single Amazon URL

"""

from .helpers.product_details import get_product_details
from docopt import docopt
import logging
import json
import os

logging.basicConfig(level=logging.INFO)

def main():
    '''entrypoint'''

    args = docopt(__doc__)

    if args["scrape"]:
        if args["--file"]:
            file_path = args["<product-url>"]
            result = get_product_details(file_path,isFile=True)
        else:
            url = args["<product-url>"]
            result = get_product_details(url)
        logging.info(json.dumps(result))
    else:
        logging.warn("No action is specified")

if __name__ == "__main__":
    main()