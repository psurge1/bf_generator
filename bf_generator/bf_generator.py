import csv

def csv_reader(path, character_encoding='utf8'):
 data=[]
 with open(path, 'r', encoding=character_encoding) as csvf:
  csvr = csv.reader(csvf)
  headers = next(csvr)

  for row in csvr:
   data.append(row)
  return data

def main():
 ascii_data = csv_reader('../ASCII_tables/ascii-table.csv')
 for row in ascii_data:
  print(row)

if __name__ == "__main__":
 main();