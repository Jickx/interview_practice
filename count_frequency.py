def count_frequency(seq):
    seq_set = set(seq)
    counter_dict = {x: 0 for x in seq_set}
    for i in seq:
        counter_dict[i] += 1
    return counter_dict


seq = [2, 3, 2, 4, 5, 6, 4, 5, 2, 4, 4, 4]

print(count_frequency(seq))
