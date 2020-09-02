#!/usr/bin/python3
import sys
import os
from parser import Parser
from code import Code
from symboltable import SymbolTable;

filename = sys.argv[1]

symbol_table = SymbolTable()

parser = Parser(filename)

current_directory = os.path.dirname(os.path.abspath(__file__))
basename = os.path.basename(filename)
outfilename = os.path.join(current_directory, os.path.splitext(basename)[0] + '.hack')
outfile = open(outfilename, 'w')

next_available_ram_address = '16'

while parser.hasMoreCommands():
    if parser.getCommandType() == 'A':
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
