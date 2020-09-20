from urllib.request import urlopen
from link_finder import LinkFinder
from general import *
import os

class Spider:
    """grab links, throw to LinkFinder

    """

    # Class variables (shared among all instances)
    project_name = ''
    base_url = ''
    domain_name = ''

    # save links to file for tracking when app stocked
    queue_file = ''
    crawled_file = ''

    # set variable for app processing
    queue_set = set()
    crawled_set = set()

    def __init__(self, project_name, base_url, domain_name):
        """initialize variables to make sure all spiders shared them
        """
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = os.path.join(project_name, 'queue.txt')
        Spider.crawled_file = os.path.join(project_name, 'crawled.txt')

        # automatically loading and operating system
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)

    @staticmethod
    def boot(self):
        """special job for the first spikder
        """

        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name)

        Spider.queue_set = file_to_set(Spider.queue_file)
        Spider.crawled_set = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        """process queue and crawled
        """

        if page_url not in Spider.crawled_set:
            print(f'{thread_name} now crawling {page_url}.')
            print(f'Queue {str(len(Spider.queue_set))} | Crawled {str(len(Spider.crawled_set))}.')
            
            # add new links to queue, remove crawled links from queue and add to crawled.
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled_set.add(page_url)

            # update queue and crawled files
            Spider.udpate_files()

    @staticmethod
    def gather_link(page_url):
        """connect to the webpage, convert machine info from links to readable info
        """

        try:
            response = urlopen(page_url)

            # get the domain urls
            if response.getheader('Content-Type') == 'text/html':
                html_string = response.read().decode('utf-8')
            finder = LinkFinder(Spider.base_url, page_url)
            find.feed(html_string)

        except:
             print("Error: an not crawl page. There isn't any links.")
        
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        """add gathered links to queue
        """

        for url in links:
            # check if url existing or domain name in url(not crawled extenal webpages)
            if url in Spider.queue_set or url in Spider.crawled_set:
                continue
            if Spider.domain_name not in url:
                continue

            Spider.queue_set.add(url)

    @staticmethod
    def update_files():
        """update queue and crawled file
        """

        set_to_file(Spider.queue_set, Spider.queue_file)
        set_to_file(Spider.crawled_set, Spider.crawled_file)
