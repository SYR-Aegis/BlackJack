# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

pic = open('img/cards-[C0]-001.xml', 'r')
soup = BeautifulSoup(pic,'html.parser')

for annotation in soup.findAll('size'):
    print(annotation['width'], annotation['height'])
    print(annotation.title.string, annotation.length.string)