from file_tools import csv_tools


a=f'++><h\nh\nh+.'

symbols={'+', '-', '>', '<', '.', ',', '[', ']'}

n=''

pointer_pos=0
pos=0
largest=0
smallest=0

ascii_dict_c = csv_tools.csv_tools.csv_reader(r'ASCII_tables\ascii-table.csv', k='asciicode')
ascii_dict_s = csv_tools.csv_tools.csv_reader(r'ASCII_tables\ascii-table.csv', k='symbol')


for i in a:
    if i in symbols:
        if i == '<':
            pos-=1
            if pos < smallest:
                smallest = pos
        elif i == '>':
            pos+=1
            if pos > largest:
                largest = pos
        n+=i

t=[0]*(largest-smallest)

output=''

for c in n:
    if c=='+':
        t[pointer_pos]+=1
    elif c=='-':
        t[pointer_pos]-=1
    elif c=='>':
        pointer_pos+=1
    elif c=='<':
        pointer_pos+=1
    elif c==',':
        t[pointer_pos]=ascii_dict_s[input()[0]]['asciicode']
    elif c=='.':
        print(ascii_dict_c[t[pointer_pos]])