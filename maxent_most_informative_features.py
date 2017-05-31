def most_informative_features(classifier, n):
    features = []
    fids = sorted(list(range(len(classifier._weights))), key=lambda fid: abs(classifier._weights[fid]), reverse=True)
    for fid in fids[:n]:
        znacajnaZnacajka, _, _ = classifier._encoding.describe(fid).partition('==')
        features.append(znacajnaZnacajka)
    return features
