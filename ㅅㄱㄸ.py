# -*- coding: utf-8 -*-

from os import listdir
import os
from bs4 import BeautifulSoup
import pandas as pd
import csv
import xml.etree.ElementTree as ET
import re


output_path = "../output"
output_file = "output/test1.csv"
if not os.path.exists(output_path):
    os.makedirs(output_path)


path = "./"
file_list = os.listdir(path)
file_list_xml = [file for file in file_list if file.endswith(".xml")]


import glob
import xml.etree.ElementTree as ET

filenames = glob.glob("/img")  # change the pattern to match your case

for filename in filenames:

       with open(filename, 'r', encoding="utf-8") as content:

           tree = ET.parse(content)

           lst_jugador = tree.findall('data_panel/players/player')

           for jugador in lst_jugador:

               print (jugador.find('name').text, jugador.get("id"))

for file in file_list_xml:
    with open(file, "rb"):
        tree = ET.parse(data)
        lst_jugador = tree.findall('data_panel/players/player')
        for jugador in lst_jugador:
           print (jugador.find('name').text, jugador.get("id"))

         filename = soup.find('filename').name
         width=soup.find('width').name
         height=soup.find('height').name
         name=soup.find('name').name
         xmin=soup.find('xmin').name
         ymin=soup.find('ymin').name
         xmax=soup.find('xmax').name
         ymax=soup.find('ymax').name
         thing=[filename, width, height, name, xmin, ymin, xmax, ymax]

         with open(output_file, 'w', newline= "") as file:
            writer=csv.writer(file)
            writer.writerow(['filename', 'width', 'height', 'name','xmin', 'ymin', 'xmax', 'ymax'])
            writer.writerow(thing)


