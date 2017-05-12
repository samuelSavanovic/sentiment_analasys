import random

import nltk
from nltk.corpus import PlaintextCorpusReader

from feature_extractors import features_all

corpus_root = 'corpora/'
wordlists = PlaintextCorpusReader(corpus_root, '.*')


def category(fileid):
    if fileid.startswith("pos_"):
        return "P"
    else:
        return "N"


documents = [(wordlists.words(fileid), cat)
             for fileid in wordlists.fileids()
             for cat in category(fileid)]

random.shuffle(documents)
featuresets = [(features_all(d), c) for (d, c) in documents]
nine = int(0.9 * len(featuresets))
train_set, test_set = featuresets[:nine], featuresets[nine:]
classifier = nltk.NaiveBayesClassifier.train(train_set)

with open("classifier_bayes_all.txt", "w") as f:
    f.write("Accuracy: " + str(nltk.classify.accuracy(classifier, test_set)))
    f.write("\n")
    for k, v in classifier.most_informative_features(15):
        f.write(k.split('_')[0] + " " + k.split('_')[-1] + "\n")
