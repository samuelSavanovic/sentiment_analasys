import re

import requests
from bs4 import BeautifulSoup


def get_links(count=50):
    url = requests.get('http://www.goodreads.com/list/show/6.Best_Books_of_the_20th_Century')
    content = url.text
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all('a', class_=re.compile("bookTitle"))
    return ["http://www.goodreads.com" + link.get('href') for link in links][:count]
