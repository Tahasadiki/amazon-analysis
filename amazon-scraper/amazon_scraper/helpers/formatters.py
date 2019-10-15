from selectorlib.formatter import Formatter

class Categories(Formatter):
    def format(self, text):
        return text.replace('\u203a',';').strip()