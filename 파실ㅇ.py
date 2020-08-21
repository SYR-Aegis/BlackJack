import glob
import csv
import re

from bs4 import BeautifulSoup

csv_file = open('test1.csv', 'w')
post_line = ['filename', 'width', 'height', 'name', 'xmin', 'ymin', 'xmax', 'ymax']
csv_writer = csv.writer(csv_file)
csv_writer.writerow(post_line)

def handle_soup(soup, csv_writer):
  filename = str(soup.find('filename'))
  filenames = re.sub('<.+?>', '', filename, 0).strip()

  width = str(soup.find('width'))
  widths = re.sub('<.+?>', '', width, 0).strip()

  height = str(soup.find('height'))
  heights = re.sub('<.+?>', '', height, 0).strip()

  name = str(soup.find('name'))
  names = re.sub('<.+?>', '', name, 0).strip()

  xmin = str(soup.find('xmin'))
  xmins = re.sub('<.+?>', '', xmin, 0).strip()

  ymin = str(soup.find('ymin'))
  ymins = re.sub('<.+?>', '', ymin, 0).strip()

  xmax = str(soup.find('xmax'))
  xmaxs = re.sub('<.+?>', '', xmax, 0).strip()

  ymax = str(soup.find('ymax'))
  ymaxs = re.sub('<.+?>', '', ymax, 0).strip()

  csv_writer.writerow([filenames, widths, heights, names, xmins, ymins, xmaxs, ymaxs])


for filename in glob.glob("img/*.xml"):
    with open(filename) as open_file:
        content = open_file.read()
        soup = BeautifulSoup(content, 'html.parser')
        handle_soup(soup, csv_writer)

csv_file.close()