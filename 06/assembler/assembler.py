#!/usr/bin/python3
import sys
import os
from parser import Parser
from code import Code
from symboltable import SymbolTable;

if len(sys.argv) == 1:
    print('You need to pass an .asm file as an argument')
    sys.exit() 
filename = sys.argv[1]
basename = os.path.basename(filename)
if os.path.splitext(basename)[1] != '.asm':
    print('The argument provided does not have the .asm extension')
    sys.exit() 

symbol_table = SymbolTable()


# first pass

parser = Parser(filename)
current_line = 0
while parser.hasMoreCommands():
    label = parser.getLabel()
    if label:
       symbol_table.updateTable(label, current_line)
    else:
        current_line += 1
    parser.advance()
del(parser)


# second pass

parser = Parser(filename)

current_directory = os.path.dirname(os.path.abspath(__file__))
outfilename = os.path.join(current_directory, os.path.splitext(basename)[0] + '.hack')
outfile = open(outfilename, 'w')

next_available_ram_address = '16'

while parser.hasMoreCommands():
    if parser.getLabel():
        # if its a label, skip this line and go to next loop iteration
        parser.advance()
        continue
    elif parser.getCommandType() == 'A':
        value = parser.address()
        if parser.isSymbol():
            # add new symbol to the table if it's not already there
            if not symbol_table.getAddress(value):
                symbol_table.updateTable(value, next_available_ram_address)
                next_available_ram_address = str(int(next_available_ram_address) + 1)
            value = symbol_table.getAddress(value)
        out = Code.toBinary(value, 16)
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
del(symbol_table)
