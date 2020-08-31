#!/usr/bin/python3
import sys
from parser import Parser

filename = sys.argv[1]
parser = Parser(filename)

while parser.hasMoreCommands():
    if parser.getCommandType() == 'A':
        print(parser.number())
    else:
        print(parser.dest())
    parser.advance()

