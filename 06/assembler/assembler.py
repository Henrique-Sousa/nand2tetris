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
        d = parser.dest() 
        c = parser.comp() 
        j = parser.jump()
        dd = Code.dest(d)
        cc = Code.comp(c)
        jj = Code.jump(j)
        out = "111" + cc + dd + jj
        print(out)
    parser.advance()

del(parser)

