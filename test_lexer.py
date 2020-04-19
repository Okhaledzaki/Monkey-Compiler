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


def TestNextToken2():
    input="let five = 5; let ten = 10; let add = fn(x, y) { x + y;};if ( 5 < 10) { return true; }"
    class struct:
        def __init__(self, expectedType, expectedLiteral):
            self.expectedType = expectedType
            self.expectedLiteral = expectedLiteral
    tests = [
        struct(tokens.LET, "let"),
        struct(tokens.IDENT, "five"),
        struct(tokens.ASSIGN, "="),
        struct(tokens.INT, "5"),
        struct(tokens.SEMICOLON, ";"),
        struct(tokens.LET, "let"),
        struct(tokens.IDENT, "ten"),
        struct(tokens.ASSIGN, "="),
        struct(tokens.INT, "10"),
        struct(tokens.SEMICOLON, ";"),
        struct(tokens.LET, "let"),
        struct(tokens.IDENT, "add"),
        struct(tokens.ASSIGN, "="),
        struct(tokens.FUNCTION, "fn"),
        struct(tokens.LPAREN, "("),
        struct(tokens.IDENT, "x"),
        struct(tokens.COMMA, ","),
        struct(tokens.IDENT, "y"),
        struct(tokens.RPAREN, ")"),
        struct(tokens.LBRACE, "{"),
        struct(tokens.IDENT, "x"),
        struct(tokens.PLUS, "+"),
        struct(tokens.IDENT, "y"),
        struct(tokens.SEMICOLON, ";"),
        struct(tokens.RBRACE, "}"),
        struct(tokens.SEMICOLON, ";"),
        struct(tokens.IF, "if"),
        struct(tokens.LPAREN, "("),
        struct(tokens.INT, "5"),
        struct(tokens.LT, "<"),
        struct(tokens.INT, "10"),
        struct(tokens.RPAREN, ")"),
        struct(tokens.LBRACE, "{"),
        struct(tokens.RETURN, "return"),
        struct(tokens.TRUE, "true"),
        struct(tokens.SEMICOLON, ";"),
        struct(tokens.RBRACE, "}"),
        struct(tokens.EOF, "")
    ]
    L = Lexer(input)

    for test in tests:
        tok = L.nextToken()
        print(tok)
        assert tok.Type == test.expectedType
        assert tok.Literal == test.expectedLiteral
    print("TestNextToken2 has passed")



TestNextToken()
TestNextToken2()
