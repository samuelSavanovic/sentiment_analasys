positive = {}
negative = {}
all = {}

with open("lexical_resource.txt") as f:
    for line in f:
        words = line.split()
        if int(words[-1]) > 0:
            positive[words[0]] = words[-1]
            all[words[0]] = ("pos", words[-1])
        else:
            negative[words[0]] = abs(int(words[-1]))
            all[words[0]] = ("neg", abs(int(words[-1])))

for k, v in all.items():
    print(k, v)
