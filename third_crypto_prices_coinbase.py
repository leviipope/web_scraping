# Navigating the HTML tree
# Contains: Tree structure, Tree siblings, Tree Parents and descendants
# Actual program: Getting crypto prices

from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents

# print(trs[0].next_sibling) # next_sibling, previous_sibling
# print(list(trs[0].next_siblings)) # next_siblings, previous_siblings -> gives generator object: smt you can iterate through -> wrap in list
# print(trs[0].parent.name)
# print(list(trs[0].descendants)) # .descendants, .contents, .children (only direct children)


# Crypto prices

prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.span.string

    prices[fixed_name] = fixed_price

print(prices)
