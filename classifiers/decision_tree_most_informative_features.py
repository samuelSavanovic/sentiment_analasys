def most_informative_features(classifier, n):
    classifier = [classifier]
    features = []
    i = 0
    while len(features) < n:
        if classifier[i]._fname != None and classifier[i]._fname not in features:
            features.append(classifier[i]._fname)
        for node in classifier[i]._decisions.values():
            if node._fname != None:
                classifier.append(node)
        i += 1
    return features
