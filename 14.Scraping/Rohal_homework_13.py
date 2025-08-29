import requests
from bs4 import BeautifulSoup
import sqlite3
import json

URL = "https://allo.ua/ua/products/mobile/proizvoditel-apple/"

try:
    response = requests.get(URL)
    response.raise_for_status()
    html_content = response.text
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit()

soup = BeautifulSoup(html_content, "html.parser")
phones = soup.find_all('a', class_= 'product-card__title')

full_phone_url = []

for phone in phones:
    full_url = phone.get('href')
    full_phone_url.append(full_url)

# print(full_phone_url)

list_about_phone = []

for link in full_phone_url:
    try:
        response = requests.get(link)
        response.raise_for_status()
        html_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit()

    phone_soup = BeautifulSoup(html_content, "html.parser")
    phone_name = phone_soup.select("h1.p-view__header-title")[0].text
    # print(phone_name)

    dict_about_phone = {}
    info_about_phone = phone_soup.select("ul.product-details__list > li")
    for info_element in info_about_phone:
        info_key = info_element.select("div.product-details__label")[0].text
        info_text = info_element.select("div.product-details__value")[0].text.strip()
        dict_about_phone[info_key] = info_text

    list_about_phone.append(dict_about_phone)

with open("phones.json", "w", encoding="utf-8") as file:
    json.dump(list_about_phone, file, indent=4)