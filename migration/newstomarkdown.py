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
content = content[1]

date = content.select("small")
date = date[0].text

removeThis = content.select('h3')
title = content.select('h3')[0].contents[0]

content.find("h3").extract()

path = "/news/" + sys.argv[1]

print("---")
print("date: {}".format(date).strip())
print("title: '{}'".format(title.strip()))
print("aliases: ['{}']".format(path))
print("---")
print(content.prettify())
