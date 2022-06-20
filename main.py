from bf_generator.bf_generator import *
from bf_interpreter.bf_interpreter import *

def main():
    # generator = bf_generator(ascii_dict_a)
    bfinterpreter = interpreter()

    with open(r"main.bf", "r") as f:
        bf_code = f.read().replace('\n', '')

    bfinterpreter.do(bf_code, print_result=True)

if __name__ == '__main__':
    main()