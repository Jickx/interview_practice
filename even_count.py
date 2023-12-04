from functools import wraps


def make_neg(fun):
    @wraps(fun)
    def wrapper(num_list):
        nums = fun(num_list)
        return [-i for i in nums]
    return wrapper


@make_neg
def even_count(length):
    is_neg = abs(length) != length
    return [-i if is_neg else i for i in range(abs(length) + 1) if i % 2 == 0]


assert even_count(-10) == [0, 2, 4, 6, 8, 10]
assert even_count(0) == [0]
assert even_count(10) == [0, -2, -4, -6, -8, -10]
