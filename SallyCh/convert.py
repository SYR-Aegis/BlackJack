import openpyxl
from bs4 import BeautifulSoup

with open(r'C:\Users\최서희\BlackJack\img\cards-[C0]-001.xml') as f_input:
    soup = BeautifulSoup(f_input, 'lxml')
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Sheet1"
ws.append(["name", "xmin", "ymin", "xmax", "ymax", "width", "height", "depth"])
name=soup.find("name")
for tag in soup.find_all("annotation"):
    ws.append([name.string, tag.xmin.string, tag.ymin.string, tag.xmax.string, tag.ymax.string, tag.width.string, tag.height.string, tag.depth.string])
wb.save(filename="card1.csv")