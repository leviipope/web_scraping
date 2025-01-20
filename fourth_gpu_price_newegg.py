# Querying multiple pages, finding products, sorting products
from sys import exception

from bs4 import BeautifulSoup
import requests, re

gpu = input("what gpu you want to search for? ")

url = f"https://www.newegg.ca/p/pl?d={gpu}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_ = "list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

items_found = {}

for page in range(1, pages + 1):
    url = f"https://www.newegg.ca/p/pl?d={gpu}&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(class_ = "item-cells-wrap border-cells short-video-box items-list-view is-list")

    items = div.find_all(string = re.compile(gpu))
    for item in items:
        parent = item.parent
        if parent.name != "a":
            continue

        link = parent['href']
        next_parent = parent.find_parent(class_="item-container")
        price = next_parent.find(class_="price-current").strong.string
        items_found[item] = {"price": int(price.replace(",", "")), "link": link}

# sorting the items

sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("-------------------")