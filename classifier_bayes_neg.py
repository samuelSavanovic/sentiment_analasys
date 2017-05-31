import nltk

from feature_set_builder import get_feature_set

train_set, test_set = get_feature_set("neg")
classifier = nltk.NaiveBayesClassifier.train(train_set)

with open("classifier_bayes_neg.txt", "w") as f:
    f.write("Accuracy: " + str(nltk.classify.accuracy(classifier, test_set)))
    f.write("\n")
    for k, v in classifier.most_informative_features(15):
        f.write(k.split('_')[0] + "\n")
