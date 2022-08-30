from abc import ABC, abstractmethod

# Abstract class for other classes
class ASTobject(ABC):
    pass

# Abstract classes
class Type(ASTobject, ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

class Function(ASTobject, ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def run(self, *args, **kwargs):
        pass

class Statement(ASTobject, ABC):
    @abstractmethod
    def __init__(self, tokens, *args, **kwargs) -> None:
        pass
    
    @abstractmethod
    def run(self):
        pass

# Types
class Str(Type):
    def __init__(self, s: str) -> None:
        val = s
        
        if val.startswith('"') and val.endswith('"'):
            val = val.replace('"', '')
        
        elif val.startswith("'") and val.endswith("'"):
            val = val.replace("'", '')
        else:
            raise RuntimeError("Invalid literal for str type!")
        self.val = val
    def __str__(self) -> str:
        return str(self.val)


class Int(Type):
    def __init__(self, s: str) -> None:
        self.val = int(s)
    def __str__(self) -> str:
        return str(self.val)


class Flo(Type):
    def __init__(self, s: str) -> None:
        self.val = float(s)
    def __str__(self) -> str:
        return str(self.val)


class Bool(Type):
    def __init__(self, s: str) -> None:
        true_false_dict = {
            "true": True,
            "false": False
        }
        try:
            self.val = true_false_dict[s]
        except KeyError:
            raise RuntimeError("Invalid literal for bool type!")
    def __str__(self) -> str:
        return "true" if self.val else "false"

# Variables
class Var:
    def __init__(self, v, name) -> None:
        self.value = v
        self.id = name


class VarIndex:
    def __init__(self, name: str) -> None:
        self.id = name

# Functions
class Print(Function):
    def __init__(self, args) -> None:
        try:
            self.arg = args[0]
        except IndexError:
            self.arg = ""
        
        try:
            self.end = args[1]
        except IndexError:
            self.end = "\n"
    
    def run(self):
        print(self.arg, end=self.end)
