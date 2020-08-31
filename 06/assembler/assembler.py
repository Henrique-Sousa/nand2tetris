#!/usr/bin/python3
from parser import Parser

parser = Parser('../add/Add.asm')

while True:
  if parser.current_command == '':
    break
  print(repr(parser.current_command))
  parser.advance()
