# def add(a, b):
#     if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
#         raise TypeError("Parameters must be numeric")
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     if b == 0:
#         raise ValueError("Divider cannot be zero")
#     return a / b
#
# def is_polindrome(text:str):
#     processed_text = "".join(list(filter(str.isalnum, text))).lower()
#     return processed_text == processed_text[::-1]
#
# is_polindrome("Some text with space")

def calculate_discount(price, discount_percentage):
    """
    Обчислює ціну після застосування знижки.
    Повертає ціну зі знижкою.
    Викликає ValueError, якщо discount_percentage не в діапазоні [0, 100].
    """
    if not (0 <= discount_percentage <= 100):
        raise ValueError("Відсоток знижки має бути від 0 до 100.")
    elif price < 0:
        raise ValueError("Ціна не може бути від'ємною.")
    return price * (1 - discount_percentage / 100)

def reverse_list(input_list):
    """Повертає новий список з елементами у зворотному порядку."""
    return input_list[::-1]

def find_max_value(numbers:list):
    """Повертає максимальне значення зі списку чисел. Повертає None для порожнього списку."""
    if not numbers:
        return None
    return max(numbers)

def format_user_name(first_name, last_name):
    """Форматує ім'я користувача як 'Прізвище, Ім'я'."""
    if not first_name and not last_name:
        raise ValueError("This can't be empty")
    elif not first_name:
        return last_name.strip()
    elif not last_name:
        return first_name.strip()
    else:
        return f"{last_name.strip()}, {first_name.strip()}"