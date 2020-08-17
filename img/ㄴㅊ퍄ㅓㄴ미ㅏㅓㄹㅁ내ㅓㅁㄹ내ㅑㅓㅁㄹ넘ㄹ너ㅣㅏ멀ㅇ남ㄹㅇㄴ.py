# -*- coding: utf-8 -*-

import os
from bs4 import BeautifulSoup
import pandas as pd
import csv
import re

output_path = "../output"
output_file = "output/test1.csv"
if not os.path.exists(output_path):
    os.makedirs(output_path)

df = pd.DataFrame(columns=['filename', 'width', 'height', 'name','xmin', 'ymin', 'xmax', 'ymax'])

xmls = open('img/cards-[C0]-001.xml')

data = xmls.read()
soup = BeautifulSoup(data, "html.parser")

filename = str(soup.find('filename'))
filenames = re.sub('<.+?>', '', filename, 0).strip()

width=str(soup.find('width'))
widths = re.sub('<.+?>', '', width, 0).strip()

height=str(soup.find('height'))
heights = re.sub('<.+?>', '', height, 0).strip()

name=str(soup.find('name'))
names = re.sub('<.+?>', '', name, 0).strip()

xmin=str(soup.find('xmin'))
xmins = re.sub('<.+?>', '', xmin, 0).strip()

ymin=str(soup.find('ymin'))
ymins = re.sub('<.+?>', '', ymin, 0).strip()

xmax=str(soup.find('xmax'))
xmaxs = re.sub('<.+?>', '', xmax, 0).strip()

ymax=str(soup.find('ymax'))
ymaxs = re.sub('<.+?>', '', ymax, 0).strip()

thing=[filenames, widths, heights, names, xmins, ymins, xmaxs, ymaxs]

with open(output_file, 'w', newline= "") as file:
    writer=csv.writer(file)
    writer.writerow(['filename', 'width', 'height', 'name','xmin', 'ymin', 'xmax', 'ymax'])
    writer.writerow(thing)


