import getpass
from lexer import *
from token import *
name = getpass.getuser()
print("Hello "+name)

while True:
    print(">> ",end="")
    line = input()
    l = Lexer(line)
    token = l.nextToken().Type
    while token is not tokens.EOF:
        print(token,end=" ")
        token = l.nextToken().Type
    print()
    

