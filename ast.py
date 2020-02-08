from abc import ABC, abstractmethod
from typing import List

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

class Program(Node):
    def __init__(self,Statements: List[Statement]):
        self.Statements = Statements
    
    def TokenLiteral(self):
        if len(self.Statements) > 0:
            return self.Statements[0].TokenLiteral()    # the first token
        else:
            return ""

    
