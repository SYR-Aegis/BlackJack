from xml.etree import ElementTree

str_xml = '''<annotation>
                <folder>img</folder>
                <filename>cards-[C0]-001.jpg</filename>
                <path>/home/eddie/study/blackjack/data/playing-cards/img/cards-[C0]-001.jpg</path>
                <source>
                    <database>Unknown</database>
                </source>
                <size>
                    <width>4128</width>
                    <height>2322</height>
                    <depth>3</depth>
                </size>
                <segmented>0</segmented>
                <object>
                    <name>10c</name>
                    <pose>Unspecified</pose>
                    <truncated>0</truncated>
                    <difficult>0</difficult>
                    <bndbox>
                        <xmin>2546</xmin>
                        <ymin>375</ymin>
                        <xmax>2902</xmax>
                        <ymax>535</ymax>
                    </bndbox>
                </object>
                <object>
                    <name>10c</name>
                    <pose>Unspecified</pose>
                    <truncated>0</truncated>
                    <difficult>0</difficult>
                    <bndbox>
                        <xmin>1566</xmin>
                        <ymin>1343</ymin>
                        <xmax>1930</xmax>
                        <ymax>1503</ymax>
                    </bndbox>
                </object>
            </annotation>'''
root_element = ElementTree.fromstring(str_xml) # 문자열에서 XML을 파싱합니다
animals = [] # 동물리스트를 저장할 list 초기화한다
iter_element = root_element.iter(tag="bndbos") # animal태그 iterator를 가져옵니다
for element in iter_element: # animal태그를 순회합니다
    animal = {} # 각 동물을 저장할 dict 초기화한다
    animal['xmin'] = element.find("xmin").text # name태그 값을 저장합니다
    animal['ymin'] = element.find("ymin").text # lefespan태그 값을 저장합니다
    animals.append(animal) # 동물리스트에 동물정보를 저장합니다
print(animals) # 결과를 출력한다

# [결과] [{'name': 'lion', 'lifespan': '13'},
#         {'name': 'tiger', 'lifespan': '17'}]