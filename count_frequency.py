from collections import Counter


def count_frequency(seq):
    return Counter(seq)


seq = [2, 3, 2, 4, 5, 6, 4, 5, 2, 4, 4, 4]

print(count_frequency(seq))
