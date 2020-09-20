# restrict only domain of base page included.

from urllib.parse import urlparse


def get_sub_domain_name(url):
    """Get the entire sub domain name (name1.name2.name3.example.com)
    
    """

    try:
        return urlparse(url).netloc
    except:
        return ''

def get_domain_name(url):
    """Get domain name (example.com), return the last element of the entire domain name
    """

    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''
