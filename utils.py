import re

# 🔹 Generator
def number_generator(n):
    for i in range(1, n + 1):
        yield i


# 🔹 Decorator (no emoji)
def logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper


# 🔹 Closure
def multiplier(x):
    def inner(y):
        return x * y
    return inner


# 🔹 Regex functions
def find_numbers(text):
    return re.findall(r"\d+", text)


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))