# xml_parser
XML parser for open data from https://proverki.gov.ru/portal/public-open-data

How to use:
1. Download and unpack 'Набор данных' (for exemple: 
    https://proverki.procrf.su/blob/plan/2021/data-20210206-structure-20181015.zip)
2. Run xml_parser.py with attributs path_to_data and INN of legal entity (for exemple: 
    python3 xml_parser.py ~/inspections 5257056035)
3. The parser will create the result XML file in ./results/ if there is any results of 
    parsing
