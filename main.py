import getpass
from lexer import *
from tokenz import *
name = getpass.getuser()
print("Hello "+name)

while True:
    print(">> ",end="")
    line = input()
    l = Lexer(line)
    tokenz = l.nextToken().Type
    while tokenz is not tokens.EOF:
        print(tokenz,end=" ")
        tokenz = l.nextToken().Type
    print()
    

