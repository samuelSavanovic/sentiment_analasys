from nltk.corpus import words as nltk_words

dictionary = dict.fromkeys(nltk_words.words(), None)


def is_english_word(word):
    global dictionary
    try:
        x = dictionary[word]
        return True
    except KeyError:
        return False


def count(lst):
    cnt = 0
    for i in lst:
        if i == True:
            cnt += 1
    return cnt


def is_english_text(text, treshold=60.0):
    """Returns whether given text has over treshold percentage of english words in it"""
    is_eng = list(map(is_english_word, text.lower().split()))
    cnt = count(is_eng)
    if cnt / len(text.split()) * 100 > treshold:
        return True
    else:
        return False
