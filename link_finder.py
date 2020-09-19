from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    # convert a relative url to a full url with domain name
                    url = parse.urljoin(self.base_url, value)

    def page_links(self):
        return self.links

    def error(self, message):
        pass


if __name__ == '__main__':
    finder = LinkFinder()
    finder.feed('<html><head><title>Countdown - NZ Supermarket - Find A Supermarket Near You</title></head></html>'
                '<body><h1>Birkhead</h1></body>')