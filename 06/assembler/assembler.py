#!/usr/bin/python3
import sys
from parser import Parser
from code import Code

filename = sys.argv[1]
parser = Parser(filename)

while parser.hasMoreCommands():
    if parser.getCommandType() == 'A':
        print(Code.toBinary(parser.number(), 16))
    else:
        print(parser.dest() + ' ' + parser.comp() + ' ' + parser.jump())
    parser.advance()

