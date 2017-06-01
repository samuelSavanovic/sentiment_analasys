import nltk

from classifiers.maxent_most_informative_features import most_informative_features
from features.feature_set_builder import get_feature_set

train_set, test_set = get_feature_set("all")
classifier = nltk.MaxentClassifier.train(train_set)
with open("classifier_maxent_all.txt", "w") as f:
    f.write("Accuracy: " + str(nltk.classify.accuracy(classifier, test_set)))
    f.write("\n")
    for k in most_informative_features(classifier, 15):
        f.write(k.split('_')[0] + " " + k.split('_')[-1] + "\n")
