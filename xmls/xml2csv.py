#! /usr/bin/python3

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import json
import sys

PATH2CSV = "../"

# extract information from *.xml and save it into *.csv
def xml_to_csv():
    '''
    path : path to the directory where xml files exists

    return : Dataframe, changes to a csv file
    '''

    xml_list = list()
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']

    for xml_file in glob.glob("*.xml"):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for member in root.findall("object"):
            value = (
                root.find("filename").text, # filename
                int(root.find("size")[0].text), # width
                int(root.find("size")[1].text), # height
                member[0].text, # class
                int(member[4][0].text), # xmin
                int(member[4][1].text), # ymin
                int(member[4][2].text), # xmax
                int(member[4][3].text), # ymax
            )
            xml_list.append(value)
    xml_df = pd.DataFrame(xml_list, columns=column_name)

    # shuffle the dataframe for better learning performance
    xml_df_shuffled = xml_df.sample(frac=1)

    return xml_df_shuffled

if __name__ == "__main__":
    xml_df = xml_to_csv()
    xml_df.to_csv(PATH2CSV+'labels.csv', index=None)
    print("csv file generated")
