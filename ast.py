from abc import ABC, abstractmethod
from typing import List                 # I will use typing hints extensively
import tokenz                            # helps a LOT in understanding things

class Node(ABC):
    @abstractmethod
    def TokenLiteral():
        pass

class Statement(Node):
    @abstractmethod
    def statementNode():
        pass

class Expression(Node):
    @abstractmethod
    def expressionNode():
        pass

########################################################

class Program(Node):
    def __init__(self,Statements: List[Statement]):
        self.Statements = Statements
    
    def TokenLiteral(self):
        if len(self.Statements) > 0:
            return self.Statements[0].TokenLiteral()    # the first tokenz
        else:
            return ""


########################################################

class Identifier(Expression):
    def __init__(self, Token: tokenz.Token, Value: str):
        self.Token = Token
        self.Value = Value
    def expressionNode():
        pass
    def TokenLiteral(self):
        return self.Token.Literal

class LetStatement(Statement):
    def __init__(self,Token: tokenz.Token ,Name: Identifier,Value: Expression):
        self.Token = Token
        self.Name = Name
        self.Value = Value
    def statementNode():
        pass
    def TokenLiteral(self):
        return self.Token.Literal


class ReturnStatement(Statement):
    def __init__(self,Token: tokenz.Token, ReturnValue: Expression):
        self.Token = Token
        self.ReturnValue = ReturnValue
    def statementNode():
        pass
    def TokenLiteral(self):
        return self.Token.Literal

        



    
