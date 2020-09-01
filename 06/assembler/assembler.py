#!/usr/bin/python3
import sys
import os
from parser import Parser
from code import Code

filename = sys.argv[1]
parser = Parser(filename)

current_directory = os.path.dirname(os.path.abspath(__file__))

basename = os.path.basename(filename)
outfilename = os.path.join(current_directory, os.path.splitext(basename)[0] + '.hack')
outfile = open(outfilename, 'w')

while parser.hasMoreCommands():
    if parser.getCommandType() == 'A':
        out = Code.toBinary(parser.number(), 16)
    else:
        d = parser.dest() 
        c = parser.comp() 
        j = parser.jump()
        dd = Code.dest(d)
        cc = Code.comp(c)
        jj = Code.jump(j)
        out = "111" + cc + dd + jj
    outfile.write(out + '\n')
    parser.advance()

outfile.close()
del(parser)

