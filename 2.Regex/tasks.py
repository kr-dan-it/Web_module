import re

# task_text_1 = "Я вивчаю python. Python - це круто!"
#
# pattern = r".ython" # <- this is the fancypants regex method
# # pattern = r"python|Python"
# # pattern = r"[Pp]ython" # same as 1st
#
# result = re.findall(pattern, task_text_1) # ["python", "Python"]
# # result = re.findall(pattern, task_text_1, re.IGNORECASE) # ignores case (pattern in this case is just "python")
#
# print(result)

# def has_https(text):
#     result = re.match(pattern2, text)
#     if result:
#         print(f"{text} starts with https://")
#     else:
#         print("Not matched")
#
# task_text_2_1 = "https://www.google.com"
# task_text_2_2 = "www.google.com"
#
# pattern2 = r"https://"
#
# has_https(task_text_2_1)
# has_https(task_text_2_2)

# task_text_3 = "Температура: 25.5 градусів. Тиск: 1012.3 гПа. Швидкість: -1.2 м/с."
# # -? = - zero or 1 times
#
# pattern = r"-?\d+\.\d*"
#
# result = re.findall(pattern, task_text_3)
# print(result)

# task_text_4 = "Контакти: alice@example.org, bob.smith@mail.com."
#
# pattern = r"\b([A-Za-z0-9._-]+)@([A-Za-z.]{1,}\b)"
#
# result = re.finditer(pattern, task_text_4)
#
# # group(0) = the whole thing
# for match_obj in result:
#     print(f"Name: {match_obj.group(1)}\nDomain: {match_obj.group(2)}")
#     print(20 * "-")
#
# # print(f"Name: {name}\nDomain: {domain}")

# task_text_5 = "Мій кіт любить спати. У мене є ще один Кіт. А де мій кіт?"
# changes_to_do = [(r"Кіт", "Пес"), (r"кіт", "пес"), (r"любить", "ненавидить")]
# # pattern = r"[Кк]іт"
# # replacement = "пес"
# result = task_text_5[:]
#
# # result = re.sub(pattern, replacement, task_text_5)
# # print(f"Original: {task_text_5}")
# # print(f"Replacement: {result}")
#
# for pattern, replacement in changes_to_do:
#     result = re.sub(pattern, replacement, result)
#
# print(result)

# task_text_6 = "Це        рядок    з   багатьма       пробілами."
#
# pattern = r"\s+"
#
# result = re.split(pattern, task_text_6)
# print(result)