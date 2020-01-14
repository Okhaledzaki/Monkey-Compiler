import enum


class tokens(enum.Enum):
    ILLEGAL="ILLEGAL"
    EOF="EOF"
    IDENT="IDENT"
    INT="INT"
    FLOAT = "FLOAT"
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"
    LT = "<"
    GT = ">"
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"
    FUNCTION = "FUNCTION"
    LET = "LET"
    TRUE = "TRUE"
    FALSE = "FALSE"
    IF = "IF"
    ELSE = "ELSE"
    RETURN = "RETURN"
    EQ = "=="
    NOT_EQ = "!="

keywords = {
    "fn": tokens.FUNCTION,
    "let": tokens.LET,
    "true": tokens.TRUE,
    "false": tokens.FALSE,
    "if": tokens.IF,
    "else": tokens.ELSE,
    "return": tokens.RETURN,
}


####################################################################################################
####################################################################################################
####################################################################################################


class Token:
    def __init__(self, Type, Literal):
        self.Type = Type
        self.Literal = Literal
    
    @staticmethod
    def isKeyword(word):
        if word in keywords:
            return keywords[word]
        return tokens.IDENT

    def __repr__(self):
        return "token->" + str(self.Type) + ":::literal->" + str(self.Literal)