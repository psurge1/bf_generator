import csv

class csv_tools:
    def __init__(self):
        pass

    def csv_reader(path, character_encoding='utf8'):
        data=[]
        with open(path, 'r', encoding=character_encoding) as csvf:
            csvr = csv.reader(csvf)
            headers = next(csvr)
        for row in csvr:
            data.append(row)
        return data