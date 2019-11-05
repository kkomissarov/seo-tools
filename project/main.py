#!/home/kkomissarov/projects/seo-tools/venv/bin/python

import argparse
from sitemap.controllers import main as run_sitemap
from crawler.controllers import main as run_crawler


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode')
    parser.add_argument('-d', '--domain')
    parser.add_argument('-u', '--url')
    parser.add_argument('-f', '--file')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    if args.mode == 'sitemap':
        run_sitemap(args)
    elif args.mode == 'crawler':
        run_crawler(args)
