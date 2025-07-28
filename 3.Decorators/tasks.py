import functools
#
# def type_checker(*expected_types):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             # Логіка перевірки типів
#             if len(args) == len(expected_types):
#                 for i in range(len(args)):
#                     if not isinstance(args[i], expected_types[i]):
#                         return None
#                 return func(*args, **kwargs)
#             else:
#                 print("Something went wrong")
#         return wrapper
#     return decorator
#
# @type_checker(str, int)
# def create_user(username, age):
#     print(f"Створено користувача: {username}, Вік: {age}")
#     return {"username": username, "age": age}
#
# @type_checker(list, float)
# def process_data_list(data, factor):
#     print(f"Обробка списку: {data} з коефіцієнтом {factor}")
#     return [x * factor for x in data]
#
# print("Тестування Завдання 1:")
# create_user("Олена", 25)
# create_user(123, "Ігор") # Має викликати попередження/помилку
# process_data_list([1.0, 2.0], 2.5)
# process_data_list("не список", 1.0) # Має викликати попередження/помилку

import time


def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        finish_time = time.perf_counter()
        execution_time = finish_time - start_time
        print(f"Функція '{func.__name__}' виконана за {execution_time:.4f} секунд.")
        return result
    return wrapper


@timer_decorator
def simulate_heavy_computation(duration_seconds):
    """Імітує важкі обчислення."""
    print(f"Починаю важкі обчислення на {duration_seconds} секунд...")
    time.sleep(duration_seconds)
    print("Обчислення завершено.")
    return "Обчислення успішні"


print("\n--- Приклад 3: Декоратор для вимірювання часу ---")

simulate_heavy_computation(0.5)
simulate_heavy_computation(0.1)