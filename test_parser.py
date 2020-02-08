import ast
import lexer
import parser



def TestLetStatements():
    input = """
    let x = 5;
    let y = 10;
    let foobar = 838383;
    """
    l = lexer.Lexer(input)
    p = parser.Parser(l)
    program = p.ParseProgram()
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
    


TestLetStatements()