positive_words = {}
negative_words = {}
all_words = {}
with open("lexical_resource.txt") as f:
    for line in f:
        words = line.split()
        if int(words[-1]) > 0:
            positive_words[words[0]] = words[-1]
            all_words[words[0]] = ("pos", words[-1])
        else:
            negative_words[words[0]] = abs(int(words[-1]))
            all_words[words[0]] = ("neg", abs(int(words[-1])))
