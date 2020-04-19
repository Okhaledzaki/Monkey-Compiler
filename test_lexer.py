from _lexer import *


def TestNextToken():
    input="=+(){},;"
    class struct:
        def __init__(self, expectedType, expectedLiteral):
            self.expectedType = expectedType
            self.expectedLiteral = expectedLiteral
    tests = [
        struct(tokens.ASSIGN,"="),
        struct(tokens.PLUS,"+"),
        struct(tokens.LPAREN,"("),
        struct(tokens.RPAREN,")"),
        struct(tokens.LBRACE,"{"),
        struct(tokens.RBRACE,"}"),
        struct(tokens.COMMA, ","),
        struct(tokens.SEMICOLON, ";"),
        struct(tokens.EOF, ""),
    ]

    L = Lexer(input)

    for test in tests:
        tok = L.nextToken()
        assert tok.Type == test.expectedType
        assert tok.Literal == test.expectedLiteral
    print("TestNextToken has passed")


TestNextToken()