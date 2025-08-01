import functools

def check_division_error(func):
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            return "Can't divide by 0."
        return func(*args, **kwargs)
    return wrapper

@check_division_error
def divide(a:int|float, b:int|float):
    return round(a/b, 2)

print(divide(-4, 2))
print(divide(8, 3))
print(divide(63, 0))
print(divide(0, 3))

# ----------------------------------------------------------------
print("-" * 30)
# ----------------------------------------------------------------

def check_index_error(func):
    functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args[1] > len(args[0]):
            return "Index out of range."
        return func(*args, **kwargs)
    return wrapper

@check_index_error
def get_element(lst:list, idx:int):
    return lst[idx]

test_list = [1, 2, 3, 4, 5]
print(get_element(test_list, 0))
print(get_element(test_list, 8))
print(get_element(test_list, 2))
print(get_element(test_list, 4))