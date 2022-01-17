import functions
from file_tools.csv_tools import csv_tools

def main():
  ascii_data = csv_tools.csv_reader(r'ASCII_tables\ascii-table.csv', k='symbol')
  py_to_bf = functions.bf_functions(ascii_data)


  py_to_bf.set_printable(True)
  py_to_bf.convert("Hello")
  py_to_bf.get_code(True)

if __name__ == "__main__":
    main();