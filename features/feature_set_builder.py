import random

from nltk.corpus import PlaintextCorpusReader

from features.feature_extractors import *

corpus_root = '../corpus'
wordlists = PlaintextCorpusReader(corpus_root, '.*')

def get_feature_set(feature_space):
    if feature_space == "pos":
        return __feature_sets(features_pos)
    elif feature_space == "neg":
        return __feature_sets(features_neg)
    else:
        return __feature_sets(features_all)


def category(fileid):
    if fileid.startswith("pos_"):
        return "P"
    else:
        return "N"


def __feature_sets(f):
    documents = [(wordlists.words(fileid), cat)
                 for fileid in wordlists.fileids()
                 for cat in category(fileid)]

    random.shuffle(documents)
    featuresets = [(f(d), c) for (d, c) in documents]
    nine = int(0.9 * len(featuresets))
    return (featuresets[:nine], featuresets[nine:])


if __name__ == "__main__":
    print("Number of tokens: ", len(set(wordlists.words())))
