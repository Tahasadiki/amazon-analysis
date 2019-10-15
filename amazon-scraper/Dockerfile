FROM python:3.7-alpine
COPY . /amazon-scraper
WORKDIR /amazon-scraper

RUN pip install -r requirements.txt

RUN pip install -e .

ENTRYPOINT ["amazon-scraper","scrape"]