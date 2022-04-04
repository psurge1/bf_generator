### This file is currently incomplete

class bf_generator:
  def __init__(self, ascii_data):
    self.ascii_data = ascii_data
    self.py_to_bf = bf_functions(self.ascii_data)

  def execute(self):
    self.py_to_bf.set_printable(True)
    self.py_to_bf.convert("Hello")
    self.py_to_bf.get_code(True)

class bf_functions:
    def __init__(self, ascii_dict):
        self.code=""
        self.__ascii_dict__=ascii_dict
        self.printable=False
        self.absolute_tape_location=0

    def __add_to_code__(self, char, num=1):
        for i in range(num):
            self.code+=char
        return

    def convert(self, arg):
        arg = str(arg)
        for char in arg:
            self.add(int(self.__ascii_dict__[char]['asciicode']))
            self.forward(1)
        # if self.printable:
        #     for i in range(self.absolute_tape_location):
                
    
    def add(self, num):
        self.__add_to_code__("+", num)

    def subtract(self, num):
        self.__add_to_code__("-", num)
    
    def forward(self, num=1):
        if (self.printable):
            self.__add_to_code__(".")
        self.__add_to_code__(">", num)
        self.absolute_tape_location+=1

    def backward(self, num=1):
        self.__add_to_code__("<", num)
    
    def get_code(self, display_to_console=False):
        if display_to_console:
            print(self.code)
        return self.code
    
    def set_printable(self, b):
        self.printable=b
    
    def input(self, num_chars):
        self.__add_to_code__(",", num_chars)