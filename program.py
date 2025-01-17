from bs4 import BeautifulSoup
import requests, re
from soupsieve.pretty import pretty

url = "https://hardverapro.hu/apro/7j8rt/friss.html"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser") # process the url as a html

price = doc.find_all("h2") # an array of finds of the h2 tags
# parent = price[0].parent # finds the parent of price[0] (= 359 990 Ft)
price_with_ft = price[0].string # get the value which is between the tags
forint = int(price_with_ft.replace(" Ft","").replace(" ", ""))
print(price_with_ft, "->", forint)