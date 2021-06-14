"""
XML parser for open data from https://proverki.gov.ru/portal/public-open-data.
How to use:
1. Download and unpack 'Набор данных' (for exemple: 
    https://proverki.procrf.su/blob/plan/2021/data-20210206-structure-20181015.zip)
2. Run xml_parser.py with attributs path_to_data and INN of legal entity (for exemple: 
    python3 xml_parser.py ~/inspections 5257056035)
3. The parser will create the result XML file in ./results/ if there is any results of 
    parsing
"""

import os
import time
from xml.etree import ElementTree
import sys
import concurrent.futures


class Parser:
    
    def __init__(self, path_to_data, inn):
        self.path_to_data = path_to_data
        self.inn = inn
        self.path_to_result = os.path.join(os.getcwd(), 'results',\
                                           f'{str(time.time())}.xml')
        self._result_root = self.result_xml()
        self.data_list = self.data_list()
        self.counter = 0
        
    def result_xml(self):
        """Creats the result xml file""" 
        if os.path.isdir(os.path.dirname(self.path_to_result)) == False:
            os.mkdir(os.path.dirname(self.path_to_result))
        with open(self.path_to_result,  'w') as f:
            f.write('<body></body>')
        _result_root = ElementTree.parse(self.path_to_result).getroot()
        return  _result_root

    def data_list(self):
        """Creats a list of XML files from path_to_data"""
        try:
            with os.scandir(self.path_to_data) as it:
                _data = [x for x in it if x.name.endswith('.xml') and x.is_file()]
                if _data == []:
                    self.deleter()
                    raise ValueError('path contains no xml files')
                else:
                    return _data
        except FileNotFoundError:
            self.deleter()
            raise ValueError('invalid path to data')

    def parser(self,  data):
        """Parses the data"""
        root = ElementTree.parse(data).getroot()
        for child in root:
            for i in range(0,  len(child)):
                try:
                    if child[i].attrib['INN'] == self.inn:
                        self._result_root.append(child)
                        self.counter += 1
                except KeyError:
                    continue
    
    def parse_the_data(self):
        """Parses the data_list"""
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.parser, self.data_list)
        if self.counter > 0:
            print(f'Find {self.counter} result(s)')
            print(f'result - {self.path_to_result}')
        else:
            print('Find nothing')

    def result(self):
        """Writes the result to the file""" 
        with open(self.path_to_result,  'w') as f:
            f.write(ElementTree.tostring(self._result_root,  'utf-8').decode())
        self.deleter()
        
    def deleter(self):
        """If the parser finds nothing or error occurred - deletes the result file"""
        with open(self.path_to_result,  'r') as f:
            r = f.read()
        if r == '<body />' or r == '<body></body>':
            print('deleting the result file')
            os.remove(self.path_to_result)

if __name__ == '__main__':
    parser = Parser(str(sys.argv[1]),  str(sys.argv[2]))
    parser.parse_the_data()
    parser.result()
