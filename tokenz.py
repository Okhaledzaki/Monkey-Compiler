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


####################################################################################################
####################################################################################################
####################################################################################################


class Token:
    def __init__(self, Type, Literal):
        self.Type = Type
        self.Literal = Literal
    
    def __repr__(self):
        return "token is: " + str(self.Type) + " and the literal is: " + str(self.Literal)