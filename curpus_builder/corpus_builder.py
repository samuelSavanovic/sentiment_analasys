from scraping.goodreads_books import get_links
from scraping.scrapper import parse_comments

if __name__ == "__main__":
    for l in get_links(10):
        comments, dates = parse_comments(l)
        i = 0
        book_name = l.split('/')[-1].split('.')[-1]
        for comment in comments:
            print(comment)
            is_pos = input("pos/neg?")
            with open("corpus/" + is_pos + "_" + book_name + "_" + dates[i] + "_" + str(i) + ".txt", "w") as f:
                f.write(comment)
            i += 1
