import re

import requests
from bs4 import BeautifulSoup

from english_checker import is_english_text


def parse_comments(link):
    url = requests.get(link)
    content = url.text
    soup = BeautifulSoup(content, 'html.parser')
    comments = soup.find_all(id=re.compile('freeText\d'))
    date = soup.find_all('a', class_=re.compile("reviewDate createdAt"))
    comments.pop(0)
    comments.pop(-1)
    comments.pop(len(comments) // 2)

    comments_text = []
    date_text = []
    # f = open('comments.txt', 'a')
    i = 0
    for l in comments:
        text = l.get_text()
        if is_english_text(text, 40.0):
            comments_text.append(text)
            date_text.append(date[i].get_text())
            # f.write(date[i].get_text())
            # f.write('\n')
            # f.write(l.get_text())
            #f.write("\n\n")

        i += 1
    # f.close()
    return comments_text, date_text
