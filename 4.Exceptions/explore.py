# import random as random
# try:
#     pass
#     # code which may have an error
# except ZeroDivisionError:
#     pass
# except ValueError as e:
#     pass
# except (IndexError, KeyError):
#     pass
# except:
#     pass
#     # error handling
# else:
#     # if try had no errors
#     pass
# finally:
#     # always completes
#     pass

# def safe_divide(numerator:int|float, denominator:int|float):
#     try:
#         result = numerator / denominator
#         print(f"{numerator} / {denominator} = {result}")
#     except ZeroDivisionError as error:
#         print(error)
#         print("Zero division")
#     except TypeError as error:
#         print("Incorrect type")
#         print(error)
#     print("Block after division")
#
# safe_divide(10, 2)
# print("-" * 30)
# safe_divide(33, 0)
# print("-" * 30)
# safe_divide("3", 4.5)

# class InvalidInputError(Exception):
#     """Exception with invalid input type"""
#     def __init__(self, message="Incorrect type of object"):
#         self.message = message
#         super().__init__(self.message)
#
# def get_user_by_id(id):
#     if id < 0:
#         raise InvalidInputError("ID is negative number")
#     return {"user_id": id, "user_name": "Test"}
#
# class InvalidUserDataError(Exception):
#     """Виняток, що виникає при некоректних даних користувача."""
#     def __init__(self, field, value, message="Некоректні дані користувача."):
#         self.field = field
#         self.value = value
#         self.message = f"{message} Поле: '{field}', Значення: '{value}'"
#         super().__init__(self.message)
#
# class DatabaseConnectionError(Exception):
#     """Виняток, що виникає при проблемах з підключенням до БД."""
#     def __init__(self, db_name, message="Помилка підключення до бази даних."):
#         self.db_name = db_name
#         self.message = f"{message} БД: '{db_name}'"
#         super().__init__(self.message)
#
# def create_new_user(username, password, email):
#     if not username or len(username) < 3:
#         raise InvalidUserDataError("username", username, "Ім'я користувача має бути не менше 3 символів.")
#     if not password or len(password) < 8:
#         raise InvalidUserDataError("password", "********","Пароль має бути не менше 8 символів.")
#     if "@" not in email:
#         raise InvalidUserDataError("email", email,"Некоректний формат email.")
#     # Імітація збереження в БД (може викликати DatabaseConnectionError)
#     if random.random() < 0.1: # 10% шанс на помилку БД
#         raise DatabaseConnectionError("main_db")
#     print(f"Користувач '{username}' успішно створений.")
#     return {"username": username, "email": email}
#
# for i in range(10):
#     username = f"test_{i}"
#     password = "pass123password"
#     email = "test@mail.com"
#
#     if i == 3:
#         username = "pp"
#     elif i == 5:
#         password = "pass"
#     elif i == 7:
#         email = "test_mail.com"
#
#     try:
#         new_user = create_new_user(username, password,  email)
#     except InvalidUserDataError as error:
#         print(f"Валідація користувача не успішна. Помилка: {error}")
#         print(f"Поле: {error.field}, Значення: {error.value}")
#     except DatabaseConnectionError as error:
#         print(f"Помилка підключення до бази данних: {error.db_name}")
#     else:
#         print(new_user)

import json
import random

def parse_json_request(json_string):
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as error:
        raise ValueError(f"Incorrect format os json_string: {error}")

def process_order_requests(request_body):
    try:
        data = parse_json_request(request_body)

        product_id = data.get("id")
        quantity = data.get("quantity", 0)

        if not isinstance(product_id, int) or product_id <= 0:
            raise ValueError("ID must be greater than 0 and not a text")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Q-ty must be greater than 0 and not a text")

        print(f"Order processed: ID: {product_id}, q-ty: {quantity}")
        return {"status": "success", "order_id": random.randint(100, 1000)}

    except ValueError as error:
        return {"status": "error", "message": error}
    except Exception as error:
        return {"status": "error", "message": "Processing error"}

order = {"id": "abc", "quantity": 4}
response = process_order_requests(json.dumps(order))
print(response)