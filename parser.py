import ast, token
from lexer import *
class Parser:
    def __init__(self,l: Lexer):
        self.l = l
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()
    
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.l.nextToken()

    def ParseProgram(self):
        return None

    
