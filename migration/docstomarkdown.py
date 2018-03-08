#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import sys
import os

with os.scandir('/home/sujee/Repositories/tw.org/html/docs') as file_iterator:
  for entry in file_iterator:
    filename, filename_extension = os.path.splitext(entry)
    if entry.is_file() and filename_extension == '.html':
      print('Reading file: {}'.format(entry.path))
      page = open(entry, 'rb')
      raw_content = page.read()
      bs = BeautifulSoup(raw_content, 'html.parser', from_encoding="utf-8")
      content = bs.select("div.main")
      content = content[0]
#      title = content.find('h3').text

      output_file = open(os.path.join('../content/page/docs', filename), 'w')
      print(output_file)
      output_file.write('---\n')
#      output_file.write('title: {}'.format(title.strip()))
#output_file.write('url: {}'.format(entry))
      output_file.write('---\n')
      output_file.close()


#print(content.prettify())
