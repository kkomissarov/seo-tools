import argparse

def clean_domain(domain):
    domain = domain.strip()

    if not(domain.startswith('http://') or domain.startswith('https://')):
        domain = 'http://' + domain

    return domain.split('//')[0] + '//' + domain.split('//')[1].split('/')[0]


if __name__ == '__main__':
    pass


