from lexpl import *
from asts import *

class Parser:
    def __init__(self, tokens, tokens_lines) -> None:
        self.tokens = tokens
        self.token_lines = tokens_lines
    
    def parse(self) -> list:
        ast = []
        
        for line in self.token_lines:
            for token in line:
                token_index = line.index(token)
                text = token[0]
                tag = token[1]
                
                types = {
                    "str": Str,
                    "int": Int,
                    "flo": Flo,
                    "bool": Bool
                }
                
                def next(num: int = 1):
                    return line[token_index + num]
                
                if tag == TYPE:
                    _ast = Var(types[text](next(3)[0]), next()[0])
                    
                    if text == "str":
                        if next(4)[0] == "+":
                            first = Str(next(3)[0])
                            second = Str(next(5)[0])
                            
                            _ast = Var(types[text](f"'{str(first)}{str(second)}'"), next()[0])
                    if text == "int":
                        _int = next(3)[0]
                        if next(4)[0] == "+":
                            first = Int(next(3)[0])
                            second = Int(next(5)[0])
                            
                            _int = first.val + second.val

                        _ast = Var(types[text](_int), next()[0])

                    ast.append(_ast)
                
                if tag == FUNCTION:
                    funcs = {
                        "print": Print
                    }

                    start = line.index(('(', RESERVED))
                    end   = line.index((')', RESERVED))
                    
                    args = line[start+1:end]
                    
                    for _iter in range(len(args)):
                        try:
                            args.remove((',', RESERVED))
                        except ValueError:
                            pass
                    
                    for i in args:
                        _types = {
                            STR: Str,
                            INT: Int,
                            BOOL: Bool,
                            FLOAT: Flo
                        }
                        
                        if i[1] == ID:
                            args[args.index(i)] = VarIndex(i[0])
                        else:
                            args[args.index(i)] = _types[i[1]](i[0])
                    
                    ast.append(funcs[text](args))
        return ast                 
