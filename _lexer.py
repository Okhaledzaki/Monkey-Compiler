from tokenz import *


class Lexer:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.readPosition = 0
        self.ch = ""
        self.readChar()
    
    def readChar(self):
        if self.readPosition >= len(self.input):
            self.ch = ""
        else:
            self.ch = self.input[self.readPosition]
        self.position = self.readPosition
        self.readPosition += 1

    def nextToken(self):
        tok = Token(None, None)
        print(self.input)
        if self.ch == "=":
            tok = Token(tokens.ASSIGN, self.ch)
        elif self.ch == "+":
            tok = Token(tokens.PLUS, self.ch)
        elif self.ch == "-":
            tok = Token(tokens.MINUS, self.ch)
        elif self.ch == "/":
            tok = Token(tokens.SLASH, self.ch)
        elif self.ch == "*":
            tok = Token(tokens.ASTERISK, self.ch)
        elif self.ch == "<":
            tok = Token(tokens.LT, self.ch)
        elif self.ch == ">":
            tok = Token(tokens.GT, self.ch)
        elif self.ch == ";":
            tok = Token(tokens.SEMICOLON, self.ch)
        elif self.ch == "(":
            tok = Token(tokens.LPAREN, self.ch)
        elif self.ch == ")":
            tok = Token(tokens.RPAREN, self.ch)
        elif self.ch == ",":
            tok = Token(tokens.COMMA, self.ch)
        elif self.ch == "{":
            tok = Token(tokens.LBRACE, self.ch)
        elif self.ch == "}":
            tok = Token(tokens.RBRACE, self.ch)
        elif self.ch == "":
            tok.Literal = ""
            tok.Type = tokens.EOF
        
        self.readChar()
        return tok


    