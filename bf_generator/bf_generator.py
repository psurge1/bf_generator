# import csv_tools

import csv, functions

def csv_reader(path, character_encoding='utf8'):
  data=[]
  with open(path, 'r', encoding=character_encoding) as csvf:
    csvr = csv.reader(csvf)
    dict_headers=next(csvr)
    dataset_dict={}
    for row in csvr:
      dataset_dict[row[1]]={dict_headers[i]:row[i] for i in [0, 2]}
    return dataset_dict

def main():
  ascii_data = csv_reader(r'ASCII_tables\ascii-table.csv')
  py_to_bf = functions.bf_functions(ascii_data)


  py_to_bf.set_printable(True)
  py_to_bf.convert("Hello")
  py_to_bf.get_code(True)

if __name__ == "__main__":
    main();