# I didn't use pytest by

import ast, _token, parser, lexer

def TestString():
    program = ast.Program(
        Statements = [
            ast.LetStatement(
                Token = _token.Token(Type=_token.tokens.LET, Literal= "let"),
                Name = ast.Identifier(
                    Token=_token.Token(
                        Type=_token.tokens.IDENT, 
                        Literal= "myVar"), 
                        Value= "myVar"),
                Value = ast.Identifier(
                    Token=_token.Token(
                        Type=_token.tokens.IDENT, 
                        Literal= "anotherVar"),
                        Value="anotherVar"))
            ])
    
    if program.String() == "let myVar = anotherVar;": print("TestString test is success")

TestString()

