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
    tests = [struct("5", 5), struct("10", 10)]
    for test in tests:
        l = lexer.Lexer(test.input)
        p = parser.Parser(l)
        program = p.ParseProgram()
        obj = evaluator.Eval(program)
        testIntegerObject(obj, test.expected)
    print("TestEvalIntegerExpression is done yaayyy")

def testIntegerObject(obj: _object.Object, expected: int) -> bool:
    assert isinstance(obj, _object.Integer)
    assert obj.Value == expected

TestEvalIntegerExpression()



