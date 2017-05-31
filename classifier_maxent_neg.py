import nltk

from feature_set_builder import get_feature_set
from maxent_most_informative_features import most_informative_features

train_set, test_set = get_feature_set("neg")
classifier = nltk.MaxentClassifier.train(train_set)
with open("classifier_maxent_neg.txt", "w") as f:
    f.write("Accuracy: " + str(nltk.classify.accuracy(classifier, test_set)))
    f.write("\n")
    for k in most_informative_features(classifier, 15):
        f.write(k.split('_')[0] + "\n")
