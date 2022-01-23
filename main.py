from utils.csv_tools import csv_tools
from bf_generator.bf_generator import *
from bf_interpreter.bf_interpreter import *

def main():
    ascii_dict_a = csv_tools.csv_reader(path=r'ASCII_tables\ascii-table.csv', k='asciicode')
    ascii_dict_s = csv_tools.csv_reader(path=r'ASCII_tables\ascii-table.csv', k='symbol')

    generator = bf_generator(ascii_dict_a)
    bfinterpreter = interpreter(ascii_dict_a, ascii_dict_s)

    bfinterpreter.do(f'++>><<><<<h\nh\nh+.')

if __name__ == '__main__':
    main()