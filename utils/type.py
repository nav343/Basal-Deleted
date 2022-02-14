from enum import Enum, auto
from utils.token import Token


class Type(Enum):
    Number = auto()
    Null = auto()
    Char = auto()

    def get_result_type(self, _other: "Type", _op: Token) -> "Type | None":
        return Type.Null
        
    def get_result_type_unary(self, _op: Token) -> "Type | None":
        return Type.Null  
        
    def __str__(self) -> str:
        match self:
            case Type.Null:
                return "Null"
            case Type.Number:
                return "int"      
