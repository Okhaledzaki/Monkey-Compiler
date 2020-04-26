import getpass
import sys
from lexer import *
from parser import *
from _token import *

def printParserErrors(errors):
    for msg in errors:
        print(msg)


name = getpass.getuser()
print("Hello "+name)
PROMPT = ">>"
while True:
    print(PROMPT, end=" ")
    line = input()
    l = Lexer(line)
    p = Parser(l)
    program = p.ParseProgram()
    if len(p.errors) != 0:
        printParserErrors(p.errors)
        continue
    print(program.String())


    

