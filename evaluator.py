import _object   # there is "object" in python
import ast
from typing import List

#
# the code is not 100% aligned with what in the book here
#

def Eval(node : ast.Node) -> _object.Object:

    if isinstance(node, ast.Program):
        return evalStatements(node.Statements)

    elif isinstance(node, ast.ExpressionStatement):
        if isinstance(node.Expression, ast.IntegerLiteral):
            return _object.Integer(Value = node.Expression.Value)
            
    return None

def evalStatements(stmts : List[ast.Statement]) -> _object.Object:
    result : _object.Object = None
    for i in range(len(stmts)):
        result = Eval(stmts[i])
    return result



