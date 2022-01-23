class interpreter:
    def __init__(self, dict1, dict2):
        self.symbols={'+', '-', '>', '<', '.', ',', '[', ']'}

        self.ascii_dict_c = dict1
        self.ascii_dict_s = dict2
    
    def reset(self):
        self.n=''
        self.pointer_pos=0
        self.pos=0
        self.largest=0
        self.smallest=0
        self.output=''


    def do(self, code_string):
        self.reset()
        for i in code_string:
            if i in self.symbols:
                if i == '<':
                    self.pos-=1
                    if self.pos < self.smallest:
                        self.smallest = self.pos
                elif i == '>':
                    self.pos+=1
                    if self.pos > self.largest:
                        self.largest = self.pos
                self.n+=i

        self.t=[0 for i in range(abs(self.largest)+abs(self.smallest)+1)]
        print(self.pos)

        print(self.t)
        for c in self.n:
            print(self.pointer_pos)
            if c=='+':
                self.t[self.pointer_pos]+=1
            elif c=='-':
                self.t[self.pointer_pos]-=1
            elif c=='>':
                self.pointer_pos+=1
            elif c=='<':
                self.pointer_pos+=1
            elif c==',':
                self.t[self.pointer_pos]=self.ascii_dict_s[input()[0]]['asciicode']
            elif c=='.':
                self.output+=self.ascii_dict_c[self.t[self.pointer_pos]]
        print(self.output)
        return self.output