from token import Token, tokens

class lexer:
    def __init__(self,input):
        self.input = input
        self.position = 0
        self.readPosition = 0
        self.ch = ""
        self.readChar()
    
    def readChar(self):
        if self.readPosition >= len(self.input):
            self.ch = None
        else:
            self.ch = self.input[self.readPosition]
        self.position = self.readPosition
        self.readPosition += 1
    
    def unreadChar(self):
        self.ch = self.input[self.position-1]
        self.position-=1
        self.readPosition-=1
    
    def skipWhitespace(self):
        while self.ch == " " or self.ch == "\t" or self.ch == "\n" or self.ch == "\r":
            self.readChar()

    def peekChar(self):
        self.skipWhitespace()
        if self.readPosition >= len(self.input):
            return None
        else:
            return self.input[self.readPosition]
    
    def readIdentifier(self):
        position = self.position
        while self.isLetter():
            self.readChar()
        self.unreadChar()
        return self.input[position:self.position+1]
    
    def readNumber(self):
        position = self.position
        while self.isDigit() or self.isDot():
            self.readChar()
        self.unreadChar()
        return self.input[position:self.position+1]

    def isLetter(self):
        return True if 'a' <= self.ch <= 'z' or 'A' <= self.ch <= 'Z' or self.ch == '_' else False
    
    def isDigit(self):
        return True if '0' <= self.ch <= '9' else False
    
    def isDot(self):
        return True if self.ch == "." else False

    def nextToken(self):
        tok = None
        self.skipWhitespace()
        if self.ch == "=":
            if self.peekChar() == "=":
                ch = self.ch
                self.readChar()
                tok = Token(tokens.EQ,"==")
            else:
                tok = Token(tokens.ASSIGN,"=")
        elif self.ch == "!":
            if self.peekChar() == "=":
                ch = self.ch
                self.readChar()
                tok = Token(tokens.BANG,"!=")
            else:
                tok = Token(tokens.ILLEGAL, self.ch)
        elif self.ch == "+":
            tok = Token(tokens.PLUS, "+")
        elif self.ch == "-":
            tok = Token(tokens.MINUS, "-")
        elif self.ch == "/":
            tok = Token(tokens.SLASH, "/")
        elif self.ch == "*":
            tok = Token(tokens.ASTERISK, "*")
        elif self.ch == "<":
            tok = Token(tokens.LT, "<")
        elif self.ch == ">":
            tok = Token(tokens.GT, ">")
        elif self.ch == ";":
            tok = Token(tokens.SEMICOLON, ";")
        elif self.ch == "(":
            tok = Token(tokens.LPAREN,"(")
        elif self.ch == ")":
            tok = Token(tokens.RPAREN,")")
        elif self.ch == ",":
            tok = Token(tokens.COMMA, ",")
        elif self.ch == "{":
            tok = Token(tokens.LBRACE, "{")
        elif self.ch == "}":
            tok = Token(tokens.RBRACE, "}")
        elif self.ch == None:
            tok = Token(tokens.EOF, "")
        else:
            if self.isLetter():
                literal = self.readIdentifier()
                tok = Token(Token.isKeyword(literal),literal)
            elif self.isDigit():
                tok = Token(tokens.INT, self.readNumber())
            else:
                tok = Token(tokens.ILLEGAL, self.ch)
        self.readChar()
        return tok
