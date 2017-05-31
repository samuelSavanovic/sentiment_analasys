import nltk

from feature_set_builder import get_feature_set

train_set, test_set = get_feature_set("all")
classifier = nltk.DecisionTreeClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
