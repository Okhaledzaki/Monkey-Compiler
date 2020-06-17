import ast
import _object
import parser
import lexer
import evaluator

def TestEvalIntegerExpression():
    class struct:
        def __init__(self, input, expected):
            self.input = input
            self.expected = expected
    tests = [struct("5", 5), struct("10", 10),
             struct("5 + 5 + 5 + 5 - 10", 10),
             struct("2 * 2 * 2 * 2 * 2", 32),
             struct("- 50 + 100 - 50", 0),
             struct("20 + 2 * -10", 0),
             struct("3 * ( 3 * 3 ) + 10", 37)]
    for test in tests:
        l = lexer.Lexer(test.input)
        p = parser.Parser(l)
        program = p.ParseProgram()
        obj = evaluator.Eval(program)
        testIntegerObject(obj, test.expected)
    print("TestEvalIntegerExpression is done yaayyy")


def TestEvalBooleanExpression():
    class struct:
        def __init__(self, input, expected):
            self.input = input
            self.expected = expected
    tests = [struct("true", True), struct("false", False)]
    for test in tests:
        l = lexer.Lexer(test.input)
        p = parser.Parser(l)
        program = p.ParseProgram()
        obj = evaluator.Eval(program)
        testBooleanObject(obj, test.expected)
    print("TestEvalBooleanExpression is done yayyy")


def TestBangOperator():
    class struct:
        def __init__(self, input, expected):
            self.input = input
            self.expected = expected
    tests = [struct("!true", False), struct("!false", True),
             struct("!5", False), struct("!!true", True),
             struct("!!false", False), struct("!-5", False)]
    for test in tests:
        l = lexer.Lexer(test.input)
        p = parser.Parser(l)
        program = p.ParseProgram()
        obj = evaluator.Eval(program)
        testBooleanObject(obj, test.expected)
    print("TestBangOperator is done yayyy")

def testBooleanObject(obj: _object.Object, expected: bool):
    assert isinstance(obj, _object.Boolean)
    assert obj.Value == expected

def testIntegerObject(obj: _object.Object, expected: int):
    assert isinstance(obj, _object.Integer)
    assert obj.Value == expected


TestEvalIntegerExpression()
TestEvalBooleanExpression()
TestBangOperator()



