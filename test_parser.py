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

def TestBooleanExpression():
    class struct:
        def __init__(self, input, expectedBoolean):
            self.input = input
            self.expectedBoolean = expectedBoolean
    tests = [struct("true;", True), struct("false;", False)]
    for test in tests:
        l = lexer.Lexer(test.input)
        p = parser.Parser(l)
        program = p.ParseProgram()
        checkParserErrors(p)
        assert len(program.Statements) == 1
        stmt = program.Statements[0]
        assert isinstance(stmt, ast.ExpressionStatement)
        boolean = stmt.Expression
        assert boolean.Value == test.expectedBoolean
    print("TestBooleanExpression test is success")


def TestIntegerLiteral(right, value):
    assert right.Value == value

def TestParsingPrefixExpression():
    class struct:
        def __init__(self, input, operator, integerValue):
            self.input = input
            self.operator = operator
            self.integerValue = integerValue
    prefixTests = [struct("!5;", "!", 5), struct("-15;", "-", 15),
                   struct("!true", "!", True), struct("!false", "!", False)]
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

def TestParsingInfixExpression():
    class struct:
        def __init__(self, input, leftValue, operator, rightValue):
            self.input = input
            self.leftValue = leftValue
            self.operator = operator
            self.rightValue = rightValue
    infixTests = [struct("5 + 5;", 5, "+", 5),
                  struct("5 - 5;", 5, "-", 5),
                  struct("5 * 5;", 5, "*", 5),
                  struct("5 / 5;", 5, "/", 5),
                  struct("5 > 5;", 5, ">", 5),
                  struct("5 < 5;", 5, "<", 5),
                  struct("5 != 5;", 5, "!=", 5),
                  struct("true == true", True, "==", True),
                  struct("true != false", True, "!=", False)]
    for test in infixTests:
        l = lexer.Lexer(test.input)
        p = parser.Parser(l)
        program = p.ParseProgram()
        checkParserErrors(p)
        assert len(program.Statements) == 1
        stmt = program.Statements[0]
        assert isinstance(stmt, ast.ExpressionStatement)
        exp = stmt.Expression
        TestIntegerLiteral(exp.Left, test.leftValue)
        assert exp.Operator == test.operator
        TestIntegerLiteral(exp.Right, test.rightValue)
    print("TestParsingInfixExpression test is success")

def TestOperatorPrecedenceParsing():
    class struct:
        def __init__(self, input, expected):
            self.input = input
            self.expected = expected
    tests = [struct("5 > 4 == 3 < 1", "((5>4)==(3<1))"),
             struct("3 < 5 == true", "((3<5)==true)"),
             struct("1 + (2 + 3) + 4", "((1+(2+3))+4)"),
             struct("2 / ( 5+ 5 )", "(2/(5+5))"),
             struct("a+add(b*c)+d","((a+add((b*c)))+d)"),
             struct("add(a+b+c*d/f+g)","add((((a+b)+((c*d)/f))+g))")]
    for test in tests:
        l = lexer.Lexer(test.input)
        p = parser.Parser(l)
        program = p.ParseProgram()
        checkParserErrors(p)
        assert program.String() == test.expected
    print("TestOperatorPrecedenceParsing test is success")

def TestIfExpression():
    input = "if (x < y) { x } else { y }"
    l = lexer.Lexer(input)
    p = parser.Parser(l)
    program = p.ParseProgram()
    checkParserErrors(p)
    assert len(program.Statements) == 1
    stmt = program.Statements[0]
    exp = stmt.Expression
    assert isinstance(exp, ast.IfExpression)
    assert exp.String() == "if(x<y) x else y"
    assert exp.Consequence.Statements[0].String() == "x"
    assert exp.Alternative.Statements[0].String() == "y"
    print("TestIfExpression test is success")

def TestFunctionalLiteralParsing():
    input = "fn(x, y) {x + y;}"
    l = lexer.Lexer(input)
    p = parser.Parser(l)
    program = p.ParseProgram()
    checkParserErrors(p)
    assert len(program.Statements) == 1
    stmt = program.Statements[0]
    function = stmt.Expression
    assert len(function.Parameters) == 2
    assert function.Parameters[0].Value == "x"
    assert function.Parameters[1].Value == "y"
    assert len(function.Body.Statements) == 1
    statement = function.Body.Statements[0]
    assert statement.String() == "(x+y)"

def TestFunctionParameterParsing():
    class struct:
        def __init__(self, input, expectedParams):
            self.input = input
            self.expectedParams = expectedParams
    tests = [struct(input = "fn() {};", expectedParams = []),
             struct(input = "fn(x) {};", expectedParams = ["x"]),
             struct(input = "fn(x, y, z) {};", expectedParams = ["x", "y", "z"])]
    for test in tests:
        l = lexer.Lexer(test.input)
        p = parser.Parser(l)
        program = p.ParseProgram()
        checkParserErrors(p)
        stmt = program.Statements[0]
        function = stmt.Expression
        assert len(function.Parameters) == len(test.expectedParams)
        for i in range(len(test.expectedParams)):
            assert function.Parameters[i].Value == test.expectedParams[i]
    print("TestFunctionParameterParsing test is success")
    

def TestCallExpressionParsing():
    input = "add(1, 2*3, 4+5);"
    l = lexer.Lexer(input)
    p = parser.Parser(l)
    program = p.ParseProgram()
    checkParserErrors(p)
    assert len(program.Statements) == 1
    stmt = program.Statements[0]
    exp = stmt.Expression
    assert exp.Function.TokenLiteral() == "add"
    assert len(exp.Arguments) == 3
    assert exp.Arguments[0].String() == 1
    assert exp.Arguments[1].String() == "(2*3)"
    assert exp.Arguments[2].String() == "(4+5)"
    print("TestCallExpressionParsing is done")

TestLetStatements()
TestReturnStatements()
TestIdentifierExpression()
TestIntegralLiteralExpression()
TestParsingPrefixExpression()
TestParsingInfixExpression()
TestBooleanExpression()
TestOperatorPrecedenceParsing()
TestIfExpression()
TestFunctionParameterParsing()
TestFunctionalLiteralParsing()
TestCallExpressionParsing()