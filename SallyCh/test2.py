# -*- coding: utf-8 -*-
import openpyxl
from bs4 import BeautifulSoup
import os
path_dir = r'C:\Users\최서희\BlackJack\img'
file_list = os.listdir(path_dir)
file_list_xml = [file for file in file_list if file.endswith(".xml")]
for item in file_list_xml:
    with open(item) as f_input:
        soup = BeautifulSoup(f_input, 'lxml')
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    ws.append(["name", "xmin", "ymin", "xmax", "ymax", "width", "height", "depth"])
    name = soup.find("name")
    for tag in soup.find_all("annotation"):
        ws.append(
            [name.string, tag.xmin.string, tag.ymin.string, tag.xmax.string, tag.ymax.string, tag.width.string,
            tag.height.string, tag.depth.string])
    wb.save(filename="card2.csv")
