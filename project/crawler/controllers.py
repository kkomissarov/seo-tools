#!/home/kkomissarov/projects/seo-tools/venv/bin/python

import argparse
import requests
from bs4 import BeautifulSoup as bs
from utils import clean_domain
from .models import session, LinksQueueItem, CrawlerItem

def get_params(parser):
    parser.add_argument('-d', '--domain')
    parser.add_argument('-f', '--file')
    parser.error('kjkj')
    namespace = parser.parse_args()
    return namespace


def main():
    parser = argparse.ArgumentParser()
    params = get_params(parser)

    domain = clean_domain(params.domain)

    new_link = LinksQueueItem(link=domain)
    session.add(new_link)
    session.commit()

if __name__ == '__main__':
    main()