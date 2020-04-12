# I did't use pytest by choice

import ast
import lexer
import parser

def checkParserErrors(p):
    errors = p.errors
    if len(errors) == 0:
        return
    else:
        print(":( sad")
    
    print("parser has {} errors".format(len(errors)))
    for msg in errors:
        print(msg)


def TestLetStatements():
    input = """
    let x = 5;
    let y = 10;
    let foobar = 838383;
    """
    l = lexer.Lexer(input)
    p = parser.Parser(l)
    program = p.ParseProgram()
    checkParserErrors(p)
    assert program != None
    assert len(program.Statements) == 3
    tests = ["x","y","foobar"]
    for i in range(3):
        stmt = program.Statements[i]
        TestLetStatement(stmt, tests[i])
    print("TestLetStatements test is success")

def TestLetStatement(stmt, test):
    assert stmt.TokenLiteral() == "let"
    assert stmt.Name.Value == test


def TestReturnStatements():
    input="""
    return 5;
    return 10;
    return 993322;
    """
    l = lexer.Lexer(input)
    p = parser.Parser(l)
    program = p.ParseProgram()
    checkParserErrors(p)
    assert len(program.Statements) == 3
    for stmt in program.Statements:
        assert stmt.TokenLiteral() == "return"
    print("TestReturnStatements test is success")


#############################################################

def TestIdentifierExpression():
    input="""
    foobar;
    """
    l = lexer.Lexer(input)
    p = parser.Parser(l)
    program = p.ParseProgram()
    checkParserErrors(p)
    assert len(program.Statements) == 1
    stmt = program.Statements[0]
    assert isinstance(stmt, ast.ExpressionStatement)
    assert stmt.Expression.TokenLiteral() == "foobar"
    print("TestIdenitiferExpression test is success")
    
def TestIntegralLiteralExpression():
    input="""
    5;
    """
    l = lexer.Lexer(input)
    p = parser.Parser(l)
    program = p.ParseProgram()
    checkParserErrors(p)
    assert len(program.Statements) == 1
    stmt = program.Statements[0]
    assert isinstance(stmt, ast.ExpressionStatement)
    literal = stmt.Expression
    assert literal.Value == 5
    assert literal.TokenLiteral() == "5"
    print("TestIntegralLiteralExpression test is success")

def TestIntegerLiteral(right, value):
    assert right.Value == value

def TestParsingPrefixExpression():
    class struct:
        def __init__(self, input, operator, integerValue):
            self.input = input
            self.operator = operator
            self.integerValue = integerValue
    prefixTests = [struct("!5;", "!", 5), struct("-15;", "-", 15)]
    for test in prefixTests:
        l = lexer.Lexer(test.input)
        p = parser.Parser(l)
        program = p.ParseProgram()
        checkParserErrors(p)
        assert len(program.Statements) == 1
        stmt = program.Statements[0]
        assert isinstance(stmt, ast.ExpressionStatement)
        exp = stmt.Expression
        assert exp.Operator == test.operator
        TestIntegerLiteral(exp.Right, test.integerValue)
        print("TestParsingPrefixExpression test is success")



TestLetStatements()
TestReturnStatements()
TestIdentifierExpression()
TestIntegralLiteralExpression()
TestParsingPrefixExpression()