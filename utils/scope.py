from typing import Type

from utils.token import Identifier


class Scope:
    __slots__ = "defined", "parent", "children"

    def register_variable(self, _name: Identifier, _type: Type):
        ...
        
    def register_function(self, _name: Identifier, _ret: Type, _args: list[Type]) -> bool:
        ...
        
    def get_variable(self, _name: Identifier) -> Type | None:
        ...
        
    def get_function(self, _name: Identifier, _args: list[Type]) -> Type | None:
        ...