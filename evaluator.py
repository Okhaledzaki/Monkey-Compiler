import _object   # there is "object" in python
import ast
from typing import List

#
# the code is not 100% aligned with what in the book here
# see the code of Eval function and you will see why ducking typing is not 
# always the best thing in the world
#

NULL  = _object.Null
TRUE  = _object.Boolean(Value = True)
FALSE = _object.Boolean(Value = False)


def Eval(node : ast.Node) -> _object.Object:

    if isinstance(node, ast.ExpressionStatement):   # here node can't be ExpressionStatement
        node = node.Expression                      # and InfixExpression at the same time
    
    if isinstance(node, ast.Program):
        return evalProgram(node.Statements)
    elif isinstance(node, ast.IntegerLiteral):
        return _object.Integer(Value = node.Value)
    elif isinstance(node, ast.Boolean):
        return _object.Boolean(Value = node.Value)
    elif isinstance(node, ast.PrefixExpression):
        right = Eval(node.Right)
        return evalPrefixExpression(node.Operator, right)
    elif isinstance(node, ast.InfixExpression):
        left = Eval(node.Left)
        right = Eval(node.Right)
        return evalInfixExpression(node.Operator, left, right)
    elif isinstance(node, ast.BlockStatement):
        return evalBlockStatement(node.Statements)
    elif isinstance(node, ast.IfExpression):
        return evalIfExpression(node)
    elif isinstance(node, ast.ReturnStatement):
        val = Eval(node.ReturnValue)
        return _object.ReturnValue(Value = val)
    return None

def evalBlockStatement(stmts : List[ast.Statement]) -> _object.Object:
    result : _object.Object = None
    for i in range(len(stmts)):
        result = Eval(stmts[i])
        if isinstance(result, _object.ReturnValue):
            return result
    return result


def evalProgram(stmts : List[ast.Statement]) -> _object.Object:
    result : _object.Object = None
    for i in range(len(stmts)):
        result = Eval(stmts[i])
        if isinstance(result, _object.ReturnValue):
            return result.Value
    return result

def evalPrefixExpression(operator : str, right : _object.Object):
    if operator == "!":
        return evalBangOperatorExpression(right)
    elif operator == "-":
        return evalMinusPrefixOperatorExpression(right)
    else:
        return NULL

def evalMinusPrefixOperatorExpression(right: _object.Object):
    if not isinstance(right, _object.Integer):
        return NULL
    value = right.Value
    return _object.Integer(Value = -value)

def evalBangOperatorExpression(right: _object.Object):
    if right == TRUE:
        return FALSE
    elif right == FALSE:
        return TRUE
    elif right == NULL:
        return TRUE
    else:
        return FALSE

def evalInfixExpression(operator: str, left: _object.Object, right: _object.Object):
    if isinstance(left, _object.Integer) and isinstance(right, _object.Integer):
        return evalIntegerInfixExpression(operator, left, right)
    if operator == "==":
        return nativeBoolToBooleanObject(left == right)
    if operator == "!=":
        return nativeBoolToBooleanObject(left != right)
    else:
        return NULL

def evalIntegerInfixExpression(operator: str, left: _object.Object, right: _object.Object):
    leftVal = left.Value
    rightVal = right.Value
    if operator == "+":
        return _object.Integer(Value = leftVal + rightVal)
    if operator == "-":
        return _object.Integer(Value = leftVal - rightVal)
    if operator == "*":
        return _object.Integer(Value = leftVal * rightVal)
    if operator == "/":
        return _object.Integer(Value = leftVal / rightVal)
    if operator == "<":
        return nativeBoolToBooleanObject(leftVal < rightVal)
    if operator == ">":
        return nativeBoolToBooleanObject(leftVal > rightVal)
    if operator == "==":
        return nativeBoolToBooleanObject(leftVal == rightVal)
    if operator == "!=":
        return nativeBoolToBooleanObject(leftVal != rightVal)
    return NULL

def nativeBoolToBooleanObject(truth):
    if truth:
        return TRUE
    return FALSE

def isTruthy(obj: _object.Object):
    if obj == NULL:
        return False
    if obj == TRUE:
        return True
    if obj == FALSE:
        return False
    return True

def evalIfExpression(ie):
    condition = Eval(ie.Condition)
    if isTruthy(condition):
        return Eval(ie.Consequence)
    elif ie.Alternative != None:
        return Eval(ie.Alternative)
    else:
        return NULL