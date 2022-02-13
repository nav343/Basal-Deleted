from abc import ABC


class Node(ABC):
    __slots__ = ()

class VarNode(Node):
    def __init__(self, name, content, token_number, line_number):
        self.name = name

class OutNode(Node):
    def __init__(self, content, token_number, line_number): pass
        
class FuncNode(Node):
    def __init__(self, name, parameters ,content, token_number, line_number):
        self.name = name
        self.parameters = parameters
        self.code = content
