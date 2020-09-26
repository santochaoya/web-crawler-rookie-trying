from urllib.request import urlopen # connect to pages

response = urlopen('https://www.countdown.co.nz/')

html_string = ''

html_string = response.read().decode('utf-8')


print(html_string)