from abc import ABC, abstractmethod
from typing import List                 # I will use typing hints extensively
import _token                            # helps a LOT in understanding things


# you maybe wondering why bother with type hints and stuff
# see evaluator and you will see its importance


class Node(ABC):
    @abstractmethod
    def TokenLiteral(self):
        pass
    def String(self):
        pass

class Statement(Node):
    @abstractmethod
    def statementNode(self):
        pass

class Expression(Node):
    @abstractmethod
    def expressionNode(self):
        pass

################################################################################

class Program(Node):
    def __init__(self,Statements: List[Statement]):
        self.Statements = Statements
    
    def TokenLiteral(self):
        if len(self.Statements) > 0:
            return self.Statements[0].TokenLiteral()    # the first _token
        else:
            return ""

    def String(self):
        out = ""
        for i in self.Statements:
            out += i.String()
        return out


################################################################################

class Identifier(Expression):
    def __init__(self, Token: _token.Token, Value: str):
        self.Token = Token
        self.Value = Value
    def expressionNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        return self.Value


################################################################################

class IntegerLiteral(Expression):
    def __init__(self, Token: _token.Token, Value: int):
        self.Token = Token
        self.Value = Value
    def expressionNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        return str(self.Value)

################################################################################

class Boolean(Expression):
    def __init__(self, Token: _token.Token, Value: bool):
        self.Token = Token
        self.Value = Value
    def expressionNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        return self.Token.Literal


################################################################################

class LetStatement(Statement):
    def __init__(self,Token: _token.Token ,Name: Identifier,Value: Expression):
        self.Token = Token
        self.Name = Name
        self.Value = Value
    def statementNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        out = ""
        out += self.TokenLiteral() + " "
        out += self.Name.String()
        out += " = "
        if self.Value:
            out += self.Value.String()
        out += ";"
        return out



################################################################################

class ReturnStatement(Statement):
    def __init__(self,Token: _token.Token, ReturnValue: Expression):
        self.Token = Token
        self.ReturnValue = ReturnValue
    def statementNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        out = ""
        out += self.TokenLiteral()
        if self.ReturnValue:
            out += self.ReturnValue.String()
        out += ";"
        return out


################################################################################

class ExpressionStatement(Statement):
    def __init__(self, Token: _token.Token, Expression: Expression):
        self.Token = Token
        self.Expression = Expression
    def statementNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        if self.Expression:
            return self.Expression.String()
        return ""

################################################################################

class PrefixExpression(Expression):
    def __init__(self, Token: _token.Token, Operator: str, Right: Expression):
        self.Token = Token
        self.Operator = Operator
        self.Right = Right
    def expressionNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        out = ""
        out += "("
        out += self.Operator
        out += self.Right.String()
        out += ")"
        return out

################################################################################

class InfixExpression(Expression):
    def __init__(self, Token: _token.Token, Left: Expression, Operator: str, Right: Expression):
        self.Token = Token
        self.Left = Left
        self.Operator = Operator
        self.Right = Right
    def expressionNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        out = ""
        out += "("
        out += str(self.Left.String())
        out += self.Operator
        out += str(self.Right.String())
        out += ")"
        return out

################################################################################

class BlockStatement(Statement):
    def __init__(self, Token: _token.Token, Statements: List[Statement]):
        self.Token = Token
        self.Statements = Statement
    def statementNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        out = ""
        for statement in self.Statements:
            out += statement.String()
        return out


################################################################################

class IfExpression(Expression):
    def __init__(self, Token: _token.Token, Condition: Expression, Consequence: BlockStatement, Alternative: BlockStatement):
        self.Token = Token
        self.Condition = Condition
        self.Consequence = Consequence
        self.Alternative = Alternative
    def expressionNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        out = ""
        out += "if"
        out += self.Condition.String()
        out += " "
        out += self.Consequence.String()
        if self.Alternative is not None:
            out += " else "
            out += self.Alternative.String()
        return out

################################################################################

class FunctionLiteral(Expression):
    def __init__(self, Token: _token.Token, Parameters: List[Identifier], Body: BlockStatement):
        self.Token = Token
        self.Parameters = Parameters
        self.Body = Body
    def expressionNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        out = ""
        params = []
        for param in self.Parameters:
            params.append(param)
        
        out += self.TokenLiteral()
        out += "("
        out += ', '.join(params)
        out += ")"
        out += self.Body.String()

        return out

################################################################################

class CallExpression(Expression):
    def __init__(self, Token: _token.Token, Function: Expression, Arguments: List[Expression]):
        self.Token = Token
        self.Function = Function
        self.Arguments = []
    def expressionNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        out = ""
        args = []
        for arg in self.Arguments:
            args.append(arg)
        
        out += self.Function.String()
        out += "("
        args = [x.String() for x in args]
        out += ", ".join(args)
        out += ")"
        return out

    


        


        



    
