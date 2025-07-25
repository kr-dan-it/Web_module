import re

# text = "Привіт, світ! Це текстовий рядок."
#
# pattern = r"світ"
#
# result = re.search(pattern, text)
#
# print(result.start())
# print(result.end())
#
# print(text[result.start(): result.end()])

# text2 = "Номер телефону: 123-456-7890 або 987-654-3210"

# pattern_2 = r"\d{3}-\d{3}-\d{4}"
# \d is any number from 0-9 (aka [0-9])
# 3 numbers from 0-9, 3 numbers from 0-9, 4 numbers from 0-9

# result = re.search(pattern_2, text2)
# # print (result.group(0))
# for i in range(1, 4):
#     print(result.group(i))

# w/o grouping
# result = re.findall(pattern_2, text2)
# print(result)
# for phone_num in result:
#     print(phone_num.split("-"))

# text4 = "Мова програмування: Python."
# text3 = "Python - чудова мова програмування."
# pattern4 = r".ython"
# result = re.match(pattern4, text3) # match only searches on the beginning ot the text
# if result:
#     print(result.group(0))
# else:
#     print("Not matched")

# text5 = "Email: test@example.com, support@domain.org, info@mail.net."
#
# # \b = word boundary (start of word)
# # + = at least 1 symbol
# # \. = search for a dot
# # \w = [A-Za-z0-9_]
# pattern = r"\b[A-Za-z-0-9._-]+@\w+\.[a-z]{2,3}\b"
# pattern_divided = r"\b([A-Za-z0-9._-]+)@(\w+\.[a-z]{2,3})\b"
#
# result = re.findall(pattern, text5)
# result_divided = re.findall(pattern_divided, text5)
# print(result)
# print(result_divided)

# text7 = "Ціни: $10.50, $25.00, $5.99."
# pattern = r"\$(\d+\.\d{2})"
#
# result = re.finditer(pattern, text7)
#
# for match_obj in result:
#     print(match_obj.group(0))
#     print(match_obj.group(1))

# text8 = "Я люблю програмувати на Python. Python - це круто."
# pattern = "Python"
# replacement = "HTML"
#
# # result = re.sub(pattern, replacement, text8)
# # print(f"Original: {text8}")
# # print(f"Replacement: {result}")
#
# result, replacement_count = re.subn(pattern, replacement, text8)
# print(f"Original: {text8}")
# print(f"Replacement: {result}")
# print(f"Number of replacement: {replacement_count}")

# text11 = "один, два; три. чотири"
#
# pattern = r"[.,;]\s*"
#
# result = re.split(pattern, text11)
# print(result)

# long_text = "Це довгий текст з багатьма словами. Слово, слово, слово. Шукаємо слово."
# compiled_pattern = re.compile(r"\bслово\b", re.IGNORECASE)
#
# result = compiled_pattern.findall(long_text)
# print(result)

text15 = "Name: Ivan, Age: 30. Name: Vadym, Age: 26."

pattern = r"Name: (?P<name>\w+), Age: (?P<age>\d+)"

# result = re.search(pattern, text15)
# if result:
#     print(result.group("name"), result.group("age"))

result = re.finditer(pattern, text15)
dict_result = {}
for i, match_obj in enumerate(result):
    name = match_obj.group("name")
    age = match_obj.group("age")
    dict_result[i] = {"name": name, "age": age}

print(dict_result)