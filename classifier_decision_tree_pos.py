import nltk

from decision_tree_most_informative_features import most_informative_features
from feature_set_builder import get_feature_set

train_set, test_set = get_feature_set("pos")
classifier = nltk.DecisionTreeClassifier.train(train_set)
features = most_informative_features(classifier, 15)

with open("classifier_decision_tree_pos.txt", "w") as f:
    f.write("Accuracy: " + str(nltk.classify.accuracy(classifier, test_set)))
    f.write("\n")
    for k in features:
        f.write(k.split('_')[0] + "\n")
