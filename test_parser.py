import ast
import lexer
import parser

def checkParserErrors(p):
    errors = p.errors
    if len(errors) == 0:
        return
    else:
        print("you fckn donkey")
    
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

    


TestLetStatements()
TestReturnStatements()