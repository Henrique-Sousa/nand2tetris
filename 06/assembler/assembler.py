#!/usr/bin/python3
import sys
from parser import Parser

filename = sys.argv[1]
parser = Parser(filename)

while True:
    if parser.current_command == '':
        break
    print(repr(parser.current_command))
    parser.advance()

