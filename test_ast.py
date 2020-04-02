# I didn't use pytest by

import ast, tokenz, parser, lexer

def TestString():
    program = ast.Program(
        Statements = [
            ast.LetStatement(
                Token = tokenz.Token(Type=tokenz.tokens.LET, Literal= "let"),
                Name = ast.Identifier(
                    Token=tokenz.Token(
                        Type=tokenz.tokens.IDENT, 
                        Literal= "myVar"), 
                        Value= "myVar"),
                Value = ast.Identifier(
                    Token=tokenz.Token(
                        Type=tokenz.tokens.IDENT, 
                        Literal= "anotherVar"),
                        Value="anotherVar"))
            ])
    
    if program.String() == "let myVar = anotherVar;": print("TestString test is success")

TestString()

