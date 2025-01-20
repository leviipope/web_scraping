# searching for tags, tag attributes, find multiple tags, find attributes, find class name, find regex, find limit, save modified html

from bs4 import BeautifulSoup
import re

with open("html/index.html", "r") as f: # opening local html file
	doc = BeautifulSoup(f, "html.parser")

# Basic usage of tags

result99 = doc.find("option") # the first find
result98 = doc.find_all("option") # array with all the finds

tag = doc.find("option") # finds the first option tag
tag["value"] = "new value" # changes the value attr to 'new value'
tag["color"] = "blue" # add a new attr
# print(tag.attrs) # all the attrs of tag

tags = doc.find_all(["p", "div", "li"]) # searching for multiple tags
tags2 = doc.find_all(["option"], string="Undergraduate", value="undergraduate") # option tag with the content of "Undergraduate" and the value attr set to "undergraduate"
tags3 = doc.find_all(class_="btn-item") # searching for class names
tags4 = doc.find_all(string=re.compile(r"\$.*"), limit = 1) # using regex and limit

# Saving the modified HTML

tags0 = doc.find_all("input", type="text")
for tag in tags0:
	tag['placeholder'] = "I changed you!"

with open("html/changed.html", "w") as file: # w mode creates or overrides
	file.write(str(doc))