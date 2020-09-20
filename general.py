import os


# create a folder for each website
def create_project_dir(directory):
    """create a folder for each separate webpage
    """

    if not os.path.exists(directory):
        print(f"Create a new folder: {directory}")
        os.mkdir(directory)


def create_data_files(project_name, base_url):
    """create queue and crawled files
    """

    # create a waiting list of links for crawling
    # file could store data that we can track when web crawler stocked. 
    queue_file = os.path.join(project_name, 'queue.txt')
    crawled_file = os.path.join(project_name, 'crawled.txt')

    if not os.path.isfile(queue_file):
        write_file(queue_file, base_url)
    if not os.path.isfile(crawled_file):
        write_file(crawled_file, '')


def write_file(path, data):
    """create a new file 
    """

    f = open(path, 'w')
    f.write(data)
    f.close


def append_to_file(path, data):
    """add data onto an existing file
    """

    with open(path, 'a') as file:
        file.write(data + '\n')


def delete_file_contents(path):
    """delete the contents of a file
    """

    with open(path, 'r'):
        pass


def file_to_set(file_name):
    """read a file and convert each line to a set
    """

    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


def set_to_file(links, file):
    """Iterate through the link set, write each item to an existing file
    """

    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)


if __name__ == '__main__':
    new_folder = create_project_dir("countdown")
    new_file = create_data_files('countdown', 'https://www.countdown.co.nz/')


