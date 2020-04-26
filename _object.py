from abc import ABC, abstractmethod
from typing import List
import enum


class obj(enum.Enum):
    INTEGER_OBJ = "INTEGER"
    BOOLEAN_OBJ = "BOOLEAN"
    NULL_OBJ    = "NULL"




class Object(ABC):
    @abstractmethod
    def Type(self):
        pass
    def Inspect(self):
        pass

################################################################################

class Integer(Object):
    def __init__(self, Value: int):
        self.Value = Value
    def Inspect(self):
        return f'{self.Value}'
    def Type(self):
        return obj.INTEGER_OBJ

################################################################################

class Boolean(Object):
    def __init__(self, Value: bool):
        self.Value = Value
    def Inspect(self):
        return f'{self.Value}'
    def Type(self):
        return obj.BOOLEAN_OBJ

################################################################################

class Null(object):
    def __init__(self):
        self.Value = None
    def Inspect(self):
        return 'null'
    def Type(self):
        return obj.NULL_OBJ

#################################################################################



