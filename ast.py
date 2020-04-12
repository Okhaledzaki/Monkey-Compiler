from abc import ABC, abstractmethod
from typing import List                 # I will use typing hints extensively
import tokenz                            # helps a LOT in understanding things

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

####################################################################

class Program(Node):
    def __init__(self,Statements: List[Statement]):
        self.Statements = Statements
    
    def TokenLiteral(self):
        if len(self.Statements) > 0:
            return self.Statements[0].TokenLiteral()    # the first tokenz
        else:
            return ""

    def String(self):
        out = ""
        for i in self.Statements:
            out += i.String()
        return out


####################################################################

class Identifier(Expression):
    def __init__(self, Token: tokenz.Token, Value: str):
        self.Token = Token
        self.Value = Value
    def expressionNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        return self.Value


####################################################################

class IntegerLiteral(Expression):
    def __init__(self, Token: tokenz.Token, Value: int):
        self.Token = Token
        self.Value = Value
    def expressionNode(self):
        pass
    def TokenLiteral(self):
        return self.Token.Literal
    def String(self):
        return str(self.Token.Value)

#####################################################################

class LetStatement(Statement):
    def __init__(self,Token: tokenz.Token ,Name: Identifier,Value: Expression):
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



#####################################################################

class ReturnStatement(Statement):
    def __init__(self,Token: tokenz.Token, ReturnValue: Expression):
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


######################################################################

class ExpressionStatement(Statement):
    def __init__(self, Token: tokenz.Token, Expression: Expression):
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

#######################################################################

class PrefixExpression(Expression):
    def __init__(self, Token: tokenz.Token, Operator: str, Right: Expression):
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

##########################################################################

class InfixExpression(Expression):
    def __init__(self, Token: tokenz.Token, Left: Expression, Operator: str, Right: Expression):
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
        out += self.Left.String()
        out += Operator
        out += self.Right.String()
        out += ")"
        return out


        


        



    
