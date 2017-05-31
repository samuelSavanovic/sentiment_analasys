from reader import positive_words, negative_words, all_words


def features_neg(text):
    return __create_features_from_text(text, negative_words)


def features_pos(text):
    return __create_features_from_text(text, positive_words)


def features_all(text):
    return __create_features_from_text(text, all_words)


def __create_features_from_text(text, feature_space):
    extracted_dict = {}
    features = set(text).intersection(feature_space)

    is_all_dict = feature_space == all_words

    for feature in features:
        count = text.count(feature)
        if is_all_dict:
            polarity, value = all_words[feature]
            key_name = feature + '_' + polarity
        else:
            value = int(feature_space[feature])
            key_name = feature

        extracted_dict[key_name] = value * count

    return extracted_dict
