import csv

class csv_tools:
    def __init__(self):
        pass

    def csv_reader(self, path, k='symbol', character_encoding='utf8'):
        p = {'asciicode':0, 'symbol':1, 'description':2}
        a = p[k]
        p.pop(k)

        with open(path, 'r', encoding=character_encoding) as csvf:
            csvr = csv.reader(csvf)
            dict_headers=next(csvr)
            dataset_dict={}
            for row in csvr:
                dataset_dict[row[a]]={dict_headers[i]:row[i] for i in p.values()}
        
        return dataset_dict