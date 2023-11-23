def merge(lst1: list, lst2: list) -> dict:
    result = {}
    for i in range(len(lst1)):
        result[lst1[i]] = lst2[i]
    return dict(sorted(result.items()))


lst1 = [3, 2, 1]
lst2 = [4, 5, 6]

print(merge(lst1, lst2))
