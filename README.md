# XML parser
XML parser for open data from https://proverki.gov.ru/portal/public-open-data

## Create and activate virtual environment, install dependencies:
```sh
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Usege:
1. Download and unpack 'Набор данных' (for exemple: 
    https://proverki.procrf.su/blob/plan/2021/data-20210206-structure-20181015.zip)
2. Run xml_parser.py with attributs path_to_data and INN of legal entity (for exemple: 
    python3 xml_parser.py ~/inspections 5257056035)
3. The parser will create the result XML file in ./results/ if there is any results of 
    parsing
    
