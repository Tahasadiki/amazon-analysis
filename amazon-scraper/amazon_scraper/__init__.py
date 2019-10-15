"""
Usage:
    amazon-analysis scrape <product-url>

Arguments:
    <product-url>   Amazon Product Details URL

"""

from .helpers.product_details import get_product_details
from docopt import docopt
import logging
import json

logging.basicConfig(level=logging.INFO)

def main():
    '''entrypoint'''

    args = docopt(__doc__)

    if args["scrape"]:
        product_details = get_product_details(args)
        logging.info(json.dumps(product_details))
    else:
        logging.warn("No action is specified")

if __name__ == "__main__":
    main()