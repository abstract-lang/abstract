from asts import *

class Runner:
    def __init__(self, ast) -> None:
        self.ast = ast
        self.variables = {}
    
    def run(self):
        for obj in self.ast:
            if isinstance(obj, Var):
                self.variables.setdefault(obj.id, obj.value)
            if isinstance(obj, Print):
                if isinstance(obj.arg, VarIndex):
                    obj.arg = self.variables[obj.arg.id]
                obj.run()
