# keep spider running as threading
# Learning notes: threading -> single worker, queue -> job list workders need to do

import threading
from queue import Queue
from spider import *
from domain import *
from general import *
import os


# make a constant variable
PROJECT_NAME = 'countdown'
HOMEPAGE = 'https://www.countdown.co.nz/'
DOMIAN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = os.path.join(PROJECT_NAME, 'queue.txt')
CRAWLED_FILE = os.path.join(PROJECT_NAME, 'crawlded.txt')
NUMBER_OF_THREADS = 8

# define a thread queue
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMIAN_NAME)








