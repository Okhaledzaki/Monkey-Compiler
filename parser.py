import ast 
from tokenz import *
from lexer import *
import time

class Parser:
    def __init__(self,l: Lexer):
        self.l = l
        self.errors = list()
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()

    def Errors(self):
        return self.errors

    def peekError(self, t: tokens):
        msg = "expected next token to be {}, got {} instead".format(t, self.peekToken.Type)
        self.errors.append(msg)

    
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
        elif self.curToken.Type == tokens.RETURN:
            return self.parseReturnStatement()
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

    def parseReturnStatement(self):
        stmt = ast.ReturnStatement(Token=self.curToken,ReturnValue=None)
        self.nextToken()

        ################
        ################
        ################

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
            self.peekError(t)
            return False

    


    
