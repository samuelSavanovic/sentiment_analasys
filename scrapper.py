import re

import urllib3
from bs4 import BeautifulSoup

from english_checker import is_english_text

http = urllib3.PoolManager()
url = http.request('GET', 'http://www.goodreads.com/book/show/5470.1984')
f = open('test.html', 'wb')
f.write(url.data)
site = open('test.html', 'r')
content = site.read()
soup = BeautifulSoup(content, 'html.parser')
comments = soup.find_all(id=re.compile('freeText\d'))
date = soup.find_all('a', class_=re.compile("reviewDate createdAt"))
comments.pop(0)
comments.pop(-1)
comments.pop(len(comments) // 2)

comments_text = []

f = open('comments.txt', 'w')
i = 0
for l in comments:
    text = l.get_text()
    if is_english_text(text, 40.0):
        comments_text.append(text)
        f.write(date[i].get_text())
        f.write('\n')
        f.write(l.get_text())
        f.write("\n\n")
    i += 1
