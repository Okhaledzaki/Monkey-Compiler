from tokenz import *


keywords = {
    "fn": tokens.FUNCTION,
    "let": tokens.LET,
    "true": tokens.TRUE,
    "false": tokens.FALSE,
    "if": tokens.IF,
    "else": tokens.ELSE,
    "return": tokens.RETURN,
}


class Lexer:
    def __init__(self, input):
        self.input = input
        self.position = 0
        self.readPosition = 0
        self.ch = ""
        self.readChar()
    
    def skipWhitespace(self):
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
            self.readChar()

    def LookupIdent(self, word):
        if word in keywords:
            return keywords[word]
        return tokens.IDENT
    
    def readChar(self):
        if self.readPosition >= len(self.input):
            self.ch = ""
        else:
            self.ch = self.input[self.readPosition]
        self.position = self.readPosition
        self.readPosition += 1
    
    def peekChar(self):
        if self.readPosition >= len(self.input):
            return ""
        else:
            return self.input[self.readPosition]

    def readIdentifier(self):
        position = self.position
        while self.isLetter():
            self.readChar()
        return self.input[position:self.position]

    def isLetter(self):
        return 'a' <= self.ch <= 'z' or 'A' <= self.ch <= 'Z' or self.ch == '_'         ## concatenating boolean operators FTW
                                                                                        ## python is the best
    def isDigit(self):
        return '0' <= self.ch <= '9'

    def readNumber(self):
        position = self.position
        while self.isDigit():
            self.readChar()
        return self.input[position:self.position]

    def nextToken(self):
        tok = Token(None, None)
        self.skipWhitespace()
        if self.ch == "=":
            if self.peekChar() == "=":
                self.readChar()
                tok = Token(tokens.EQ,"==")
            else:
                tok = Token(tokens.ASSIGN,"=")
        elif self.ch == "!":
            if self.peekChar() == "=":
                self.readChar()
                tok = Token(tokens.NOT_EQ,"!=")
            else:
                tok = Token(tokens.BANG, self.ch)
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
        else:
            if self.isLetter():
                Identifier = self.readIdentifier()
                Type = self.LookupIdent(Identifier)
                return Token(Type, Identifier)
            if self.isDigit():
                Type = tokens.INT
                Literal = self.readNumber()
                return Token(Type, Literal)
            else:
                return Token(tokens.ILLEGAL, self.ch)
        self.readChar()
        return tok


    