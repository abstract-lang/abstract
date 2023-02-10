from typing import Callable, TypeAlias, Any
from abc import ABC, abstractmethod

FunctionCallback: TypeAlias = Callable

VarName: TypeAlias = str 
TypeName: TypeAlias = str

VType: TypeAlias = str
RType: TypeAlias = str

class ASTobject(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None: ...
    @abstractmethod
    def _eval_(self, *args, **kwargs) -> Any: ...

class Type(ASTobject):
    def __init__(self, name: TypeName) -> None:
        self.name = name
    def _eval_(self, *args, **kwargs) -> Any:
        return super()._eval_(*args, **kwargs)

class Argument(ASTobject):
    def __init__(self, name: VarName, vtype: VType) -> None:
        self.name = name
        self.vtype = vtype
    def _eval_(self, *args, **kwargs) -> Any:
        return super()._eval_(*args, **kwargs)

class Signature(ASTobject):
    def __init__(self, *args: list[Argument], rtype: RType) -> None:
        self.args = args
        self.rtype = rtype
    def _eval_(self, *args, **kwargs) -> Any:
        return super()._eval_(*args, **kwargs)

class Function(ASTobject):
    def __init__(self, signature: Signature) -> None:
        self.signature = signature
    def _eval_(self, *args, **kwargs):
        raise NotImplementedError('This method is not implemented!')
