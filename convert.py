def convert(n):
    result = []
    for i in range(n + 1):
        result.append(str(i))

    return f"{''.join(result)}"


print(convert(23))
