from urllib.request import urlopen # connect to pages

response = urlopen('https://www.countdown.co.nz/shopping-made-easy')

if tag == 'a':
    for (attribute, value) in attrs:
        if attribute == 'href':
            # convert a relative url to a full url with domain name
            url = parse.urljoin(self.base_url, value)

print(response.read().decode('utf-8'))