#!/usr/bin/python3
import sys
from parser import Parser

filename = sys.argv[1]
parser = Parser(filename)

while parser.hasMoreCommands():
    print(parser.current_command)
    parser.advance()

