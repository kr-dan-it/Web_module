# Напишіть функцію `get_positive_integer()`, яка просить користувача ввести ціле число.
# Використайте `try-except` для обробки `ValueError`, якщо введено не число,
# та `TypeError`, якщо введено від'ємне число.
# Повторюйте запит, доки не отримаєте валідне додатне число.

# def get_positive_integer():
#     while True:
#         try:
#             user_input = int(input("Enter a positive number: "))
#             print(user_input)
#             if user_input <= 0:
#                 raise TypeError
#             break
#         except ValueError as error:
#             print("Value error happened, try again. ")
#         except TypeError as error:
#             print("Type error happened, try again. ")
#
# get_positive_integer()

# def get_positive_integers(n=1):
#     if n > 1:
#         total_digits = []
#     for i in range(n):
#         while True:
#             try:
#                 digit = int(input("Enter digit: "))
#                 if digit < 0:
#                     raise TypeError("Digit must be positive.")
#             except (ValueError, TypeError) as error:
#                 print(error)
#             else:
#                 if n == 1:
#                     return digit
#                 elif n > 1:
#                     total_digits.append(digit)
#                     print(f"Digit {digit} added to list.")
#                     break
#     return total_digits
#
# print(get_positive_integers())

# Уявіть, що ви обробляєте список URL-адрес. Деякі з них можуть бути некоректними #
# або викликати мережеві помилки.
# Напишіть функцію `process_urls(url_list)`, яка:
# 1. Ітерує по списку URL.
# 2. Для кожного URL імітує мережевий запит (можна просто `print()` або викликати `requests.get()` для реального тестування).
# 3. Обробляє `requests.exceptions.ConnectionError` (якщо URL недоступний) та `requests.exceptions.Timeout` (якщо запит завис).
# 4. Для кожної помилки логуйте її та продовжуйте обробку наступного URL.
# 5. Поверніть список успішно оброблених URL.

import requests
# Імітація requests для завдання

class MockRequests:
    def get(self, url, timeout=5):
        if "error" in url:
            raise requests.exceptions.ConnectionError(f"Failed to connect to {url}")
        if "timeout" in url:
            raise requests.exceptions.Timeout(f"Request to {url} timed out")
        if "404" in url:
            resp = requests.Response()
            resp.status_code = 404
            resp.url = url
            raise requests.exceptions.HTTPError(response=resp)
        print(f"Успішний запит до {url}")
        return type('obj', (object,), {'status_code': 200, 'text': f"Content from {url}", "url": url})()

def process_urls(url_list):
    my_requests = MockRequests()
    response_list = []
    for url in url_list:
        try:
            response = my_requests.get(url)
        except(requests.exceptions.ConnectionError, requests.exceptions.Timeout) as error:
            print(error)
        except requests.exceptions.HTTPError as error:
            print(f"Status code: {error.response.status_code}, URL: {error.response.url}")
        else:
            response_list.append(response)
    return response_list

urls_to_process = [
    "http://valid.com/page1",
    "http://error.com/page2",
    # Імітація ConnectionError
    "http://valid.com/page3",
    "http://timeout.com/page4",
    # Імітація Timeout
    "http://valid.com/page5",
    "http://404.com/page6"
    # Імітація HTTPError (404)
    ]
processed_urls = process_urls(urls_to_process)
print([f"Успішно оброблені URL: {url.url}" for url in processed_urls])

# my_requests = MockRequests()
# response = my_requests.get(urls_to_process[0])
# print(response)