#!/home/kkomissarov/projects/seo-crawler/venv/bin/python

import argparse
import requests
from bs4 import BeautifulSoup as bs
from utils import clean_domain
import re


def get_params(parser):
    parser.add_argument('-d', '--domain')
    parser.add_argument('-u', '--url')
    parser.add_argument('-f', '--file')
    namespace = parser.parse_args()
    return namespace


def get_robots_by_domain(domain):
    url = domain + '/robots.txt'
    response = requests.get(url)
    result = response.text if response.ok else None
    return result


def get_sitemap_url_by_robots(robots):
    url = re.findall(r'sitemap:(.*)', robots.lower())[0].strip()
    return url


def validate_params(params):
    error_msg = None

    if params.domain and params.url:
        error_msg = 'Нельзя использовать --domain и --url одновременно. Вы должны использовать один из этих параметров.'

    if not params.domain and not params.url:
        error_msg = 'Не указан источник карты сайта. Используйте --domain для автоматического поиска карты сайта или '\
                    '--url, чтобы указать адрес карты сайта вручную.'

    return error_msg


def get_sitemap_url(params):
    if params.domain:
        domain = clean_domain(params.domain)
        robots = get_robots_by_domain(domain)
        if not robots:
            return None
        sitemap_url = get_sitemap_url_by_robots(robots)
        if not sitemap_url:
            return None
    else:
        sitemap_url = params.url
    return sitemap_url


def parse_sitemap(sitemap_url):
    sitemap = requests.get(sitemap_url).text
    soup = bs(sitemap, 'lxml')
    urls = [url.text for url in soup.find_all('loc')]

    result = []
    for url in urls:
        if url.endswith('.xml'):
            result += parse_sitemap(url)
        else:
            result.append(url)
    return result


def main():
    parser = argparse.ArgumentParser()
    params = get_params(parser)

    error_msg = validate_params(params)
    if error_msg:
        parser.error(error_msg)

    sitemap_url = get_sitemap_url(params)
    if not sitemap_url:
        error_msg = 'Не удалось получить адрес карты сайта'
        parser.error(error_msg)

    print('Получаем список url. Это может занять некоторое время.')
    urls = parse_sitemap(sitemap_url)

    if params.file:
        with open(params.file, 'w') as result:
            for url in urls:
                result.write(f'{url}\n')
    else:
        for url in urls:
            print(url)


if __name__ == '__main__':
    main()


