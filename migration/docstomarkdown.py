#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

f = open(sys.argv[1])
c = f.read()
s = BeautifulSoup(c, 'html.parser', from_encoding="utf-8")
content = s.select("div.main")
content = content[0]

title = content.find('h3').text

content.find("h3").extract()

path = "/docs/" + sys.argv[1]

print("---")
print("title: \"{}\"".format(title.strip()))
print("url: '{}'".format(path))
print("---")
print(content.prettify())
