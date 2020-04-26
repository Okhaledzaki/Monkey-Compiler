import ast 
from _token import *        # because there is "token" in python
from lexer import *
from utilities import *
import time




class Parser:
    def __init__(self,l: Lexer):
        self.l = l
        self.errors = list()
        self.curToken = None
        self.peekToken = None
        self.operators = enum(
                'LOWEST',
                'EQUALS',
                'LESSGREATER',
                'SUM',
                'PRODUCT',
                'PREFIX',
                'CALL'
        )
        self.precedences = {
            tokens.EQ : self.operators.EQUALS,
            tokens.NOT_EQ : self.operators.EQUALS,
            tokens.LT : self.operators.LESSGREATER,
            tokens.GT : self.operators.LESSGREATER,
            tokens.PLUS : self.operators.SUM,
            tokens.MINUS : self.operators.SUM,
            tokens.SLASH : self.operators.PRODUCT,
            tokens.ASTERISK : self.operators.PRODUCT,
            tokens.LPAREN: self.operators.CALL
        }
        self.prefixParseFns = dict()
        self.infixParseFns = dict()
        self.initializeParseFns()
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

    def initializeParseFns(self):
        self.prefixParseFns[tokens.IDENT] = self.parseIdentifier
        self.prefixParseFns[tokens.INT] = self.parseIntegerLiteral
        self.prefixParseFns[tokens.MINUS] = self.parsePrefixExpression
        self.prefixParseFns[tokens.BANG] = self.parsePrefixExpression
        self.prefixParseFns[tokens.TRUE] = self.parseBoolean
        self.prefixParseFns[tokens.FALSE] = self.parseBoolean
        self.prefixParseFns[tokens.LPAREN] = self.parseGroupedExpression
        self.prefixParseFns[tokens.IF] = self.parseIfExpression
        self.prefixParseFns[tokens.FUNCTION] = self.parseFunctionLiteral

        self.infixParseFns[tokens.PLUS] = self.parseInfixExpression
        self.infixParseFns[tokens.MINUS] = self.parseInfixExpression
        self.infixParseFns[tokens.SLASH] = self.parseInfixExpression
        self.infixParseFns[tokens.ASTERISK] = self.parseInfixExpression
        self.infixParseFns[tokens.EQ] = self.parseInfixExpression
        self.infixParseFns[tokens.NOT_EQ] = self.parseInfixExpression
        self.infixParseFns[tokens.LT] = self.parseInfixExpression
        self.infixParseFns[tokens.GT] = self.parseInfixExpression
        self.infixParseFns[tokens.LPAREN] = self.parseCallExpression

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
            return self.parseExpressionStatement()

    def parseExpression(self, precedence):
        if self.curToken.Type in self.prefixParseFns:
            prefix = self.prefixParseFns[self.curToken.Type]
        else:
            self.noPrefixParseFnError(self.curToken.Type)
            return None
        leftExp = prefix()
        while not self.peekTokenIs(tokens.SEMICOLON) and precedence < self.peekPrecedence():
            if self.peekToken.Type in self.infixParseFns:
                infix = self.infixParseFns[self.peekToken.Type]
            else:
                return leftExp
            self.nextToken()
            leftExp = infix(leftExp)

        return leftExp

    def parsePrefixExpression(self):
        expression = ast.PrefixExpression(Token= self.curToken, Operator= self.curToken.Literal, Right = None)
        self.nextToken()
        expression.Right = self.parseExpression(self.operators.PREFIX)
        return expression

    def parseInfixExpression(self, left: ast.Expression):
        expression = ast.InfixExpression(Token= self.curToken, Left= left, Operator= self.curToken.Literal, Right=None)
        precedence = self.curPrecedence()
        self.nextToken()
        expression.Right = self.parseExpression(precedence)
        return expression


    def parseIdentifier(self):
        return ast.Identifier(Token = self.curToken, Value= self.curToken.Literal)

    def parseBoolean(self):
        return ast.Boolean(Token = self.curToken, Value= self.curTokenIs(tokens.TRUE))

    def parseGroupedExpression(self):
        self.nextToken()
        exp = self.parseExpression(self.operators.LOWEST)
        if not self.expectPeek(tokens.RPAREN):
            return None
        return exp

    def parseIfExpression(self):
        expression = ast.IfExpression(Token=self.curToken, Condition = None, Consequence = None, Alternative = None)
        
        if not self.expectPeek(tokens.LPAREN):
            return None

        self.nextToken()

        expression.Condition = self.parseExpression(self.operators.LOWEST)
        if not self.expectPeek(tokens.RPAREN):
            return None
        
        if not self.expectPeek(tokens.LBRACE):
            return None
        
        expression.Consequence = self.parseBlockStatement()

        if self.peekTokenIs(tokens.ELSE):
            self.nextToken()

            if not self.expectPeek(tokens.LBRACE):
                return None
            
            expression.Alternative = self.parseBlockStatement()
        
        return expression
    

    def parseBlockStatement(self):
        block = ast.BlockStatement(Token=self.curToken, Statements= None)
        Statements = []
        self.nextToken()

        while not self.curTokenIs(tokens.RBRACE) and not self.curTokenIs(tokens.EOF):
            stmt = self.parseStatement()
            if stmt is not None:
                Statements.append(stmt)
            self.nextToken()
        block.Statements = Statements
        return block
        
        

    def parseIntegerLiteral(self):
        lit = ast.IntegerLiteral(Token = self.curToken, Value=None)
        try:
            value = int(self.curToken.Literal)
        except:
            msg = "The integer couldn't be parsed"
            self.errors.append(msg)
            return None
        lit.Value = value
        return lit

    def parseFunctionLiteral(self):
        lit = ast.FunctionLiteral(Token= self.curToken, Parameters=None, Body=None)
        if not self.expectPeek(tokens.LPAREN):
            return None
        
        lit.Parameters = self.parseFunctionParameters()

        if not self.expectPeek(tokens.LBRACE):
            return None

        lit.Body = self.parseBlockStatement()

        return lit

    def parseCallExpression(self, function):
        exp = ast.CallExpression(Token = self.curToken, Function = function, Arguments = [])
        exp.Arguments = self.parseCallArguments()
        return exp

    def parseCallArguments(self):
        args = []
        if self.peekTokenIs(tokens.RPAREN):
            self.nextToken()
            return args
        
        self.nextToken()
        args.append(self.parseExpression(self.operators.LOWEST))

        while self.peekTokenIs(tokens.COMMA):
            self.nextToken()
            self.nextToken()
            args.append(self.parseExpression(self.operators.LOWEST))
        
        if not self.expectPeek(tokens.RPAREN):
            return None
        
        return args

    def parseFunctionParameters(self):
        identifiers = list()
        if self.peekTokenIs(tokens.RPAREN):
            self.nextToken()
            return identifiers
        self.nextToken()

        ident = ast.Identifier(Token=self.curToken, Value=self.curToken.Literal)
        identifiers.append(ident)

        while self.peekTokenIs(tokens.COMMA):
            self.nextToken()
            self.nextToken()
            ident = ast.Identifier(Token=self.curToken, Value=self.curToken.Literal)
            identifiers.append(ident)
        
        if not self.expectPeek(tokens.RPAREN):
            return None

        return identifiers

    def parseLetStatement(self):
        stmt = ast.LetStatement(Token=self.curToken,Name=None,Value=None)

        if not self.expectPeek(tokens.IDENT):
            return None
        
        stmt.Name = ast.Identifier(Token=self.curToken,Value=self.curToken.Literal)
        if not self.expectPeek(tokens.ASSIGN):
            return None
        
        self.nextToken()

        stmt.Value = self.parseExpression(self.operators.LOWEST)

        while not self.curTokenIs(tokens.SEMICOLON):
            self.nextToken()
        
        return stmt

    def parseReturnStatement(self):
        stmt = ast.ReturnStatement(Token=self.curToken,ReturnValue=None)
        self.nextToken()

        stmt.ReturnValue = self.parseExpression(self.operators.LOWEST)

        while not self.curTokenIs(tokens.SEMICOLON):
            self.nextToken()
        
        return stmt

    def parseExpressionStatement(self):
        stmt = ast.ExpressionStatement(Token=self.curToken,Expression=None)
        stmt.Expression = self.parseExpression(self.operators.LOWEST)
        
        if self.peekTokenIs(tokens.SEMICOLON):
            self.nextToken()

        return stmt

    ######################################################################

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
    
    def peekPrecedence(self):
        if self.peekToken.Type in self.precedences:
            return self.precedences[self.peekToken.Type]
        else:
            return self.operators.LOWEST
    
    def curPrecedence(self):
        if self.curToken.Type in self.precedences:
            return self.precedences[self.curToken.Type]
        else:
            return self.operators.LOWEST

    def noPrefixParseFnError(self, t : tokens):
        msg = f"no prefix parse function {t} :("
        self.errors.append(msg)




    


    
