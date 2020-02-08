import ast 
from tokenz import *
from lexer import *
import time

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
        program = ast.Program(None)
        program.Statements = list()
        while self.curToken.Type != tokens.EOF:
            stmt = self.parseStatement()
            if stmt:
                program.Statements.append(stmt)
            self.nextToken()
        
        return program

    def parseStatement(self):
        if self.curToken.Type == tokens.LET:
            return self.parseLetStatement()
        else:
            return None

    def parseLetStatement(self):
        stmt = ast.LetStatement(Token=self.curToken,Name=None,Value=None)

        if not self.expectPeek(tokens.IDENT):
            return None
        
        stmt.Name = ast.Identifier(Token=self.curToken,Value=self.curToken.Literal)
        if not self.expectPeek(tokens.ASSIGN):
            return None
        
        ###############
        ###############
        ###############

        while not self.curTokenIs(tokens.SEMICOLON):
            self.nextToken()
        
        return stmt

    def curTokenIs(self, t: tokens):
        return self.curToken.Type == t

    def peekTokenIs(self, t: tokens):
        return self.peekToken.Type == t

    def expectPeek(self,t: tokens):
        if self.peekTokenIs(t):
            self.nextToken()
            return True
        else:
            return False

    


    
