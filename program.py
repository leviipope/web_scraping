from bs4 import BeautifulSoup
import requests, re
from soupsieve.pretty import pretty

url = "https://hardverapro.hu/apro/7j8rt/friss.html"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

price = doc.find_all("h2") # print(price)
# parent = price[0].parent
price_with_ft = price[0].string
forint =  int(re.sub(r'\D', '',price_with_ft))
print(price_with_ft, "->", forint)