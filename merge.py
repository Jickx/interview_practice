def merge(lst1: list, lst2: list) -> dict:
    return dict(sorted(zip(lst1, lst2)))


lst1 = [2, 3, 1]
lst2 = ['a', 'b', 'c']

print(merge(lst1, lst2))
