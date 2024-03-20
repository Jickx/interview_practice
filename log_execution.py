def log_execution(func):
    def wrapper(a, b):
        print(f'Executing function: {func.__name__}')
        print(f'Arguments: {a, b}')
        return func(a, b)

    return wrapper


@log_execution
def add_numbers(a, b):
    return a + b


# Test the decorator
result = add_numbers(3, 5)
print("Result:", result)

# Executing function: add_numbers
# Arguments: (3, 5)
# Result: 8
