from goodreads_books import get_links
from reader import positive_words, negative_words
from scrapper import parse_comments


def features(words, text):
    freqs = {}
    for word in words:
        word = word.lower()
        count = text.count(word)
        if count > 0:
            freqs[word] = count * int(words[word])
    return freqs


def features_pos(text):
    return features(positive_words, text)


def features_neg(text):
    return features(negative_words, text)


def features_all(text):
    positive = features(positive_words, text)
    negative = features(negative_words, text)
    suf_p = list(map(lambda x: x + "_pos", positive))
    suf_n = list(map(lambda x: x + "_neg", negative))
    for s in suf_p:
        positive[s] = positive.pop(s[0:-4])
    for s in suf_n:
        negative[s] = negative.pop(s[0:-4])
    all = positive.copy()
    all.update(negative)
    return all


comments, dates = parse_comments(get_links(1)[0])
all = features_all(comments[0])

for k, v in all.items():
    print(k, v)
