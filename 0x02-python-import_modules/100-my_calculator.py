#!/usr/bin/python
import sys
if __name__ == '__main__':
    nargs = len(sys.argv)-1

    if nargs != 3:
        print('usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    op = sys.argv[2]
    if op not in('+', '-', '*', '/'):
        print('uknown operator.Available operatos:+,*,- and /')
        sys.exit(1)
    from calculator_1 import add,sub,mul,div    
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == '+':
        print('{:d} + {:d} = {:d}'.format(a, b, add(a,b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
    
