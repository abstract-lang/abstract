from abst_lexer import *

class ASTcreator:
    def __init__(self, token_lines):
        self.token_lines = token_lines
    
    def build(self) -> dict:
        result = {}
        
        for i in self.token_lines:
            result.setdefault(str(self.token_lines.index(i) + 1), i)
        
        for _line_index in result.keys():
            _line = result[_line_index]
            
            for _token in _line:
                if _token[1] == FUNCTION:
                    if not _line[_line.index(_token) + 2][0] == ")":
                        _args_tokens = []
                        
                        # _line[_line.index(_token) + 1][0] == "("
                        
                        for _arg in _line[_line.index(_token) + 2:]:
                            if _arg[0] == ")":
                                break
                            elif _arg[0] == ",":
                                pass
                            else:
                                _args_tokens.append(_arg)
                        
                        _args = []
                        
                        for _arg_token in _args_tokens:
                            if _arg_token[1] == ID:
                                _args.append({
                                    "id": _arg_token[0]
                                })
                            else:
                                _args.append({
                                    "literal": {
                                        "type": str(_arg_token[1]).lower(),
                                        "value": str(_arg_token[0])
                                    }
                                })
                        
                        
                        result[_line_index] = {
                            str(_token[0]): {
                                "args": _args
                            }
                        }
                    else:
                        result[_line_index] = {
                            str(_token[0]): {
                                "args": []
                            }
                        }
                if _token[1] == TYPE:
                    _type = _token[0]
                    _id = _line[_line.index(_token) + 1]
                    _value = _line[_line.index(_token) + 3]
                    
                    if _value[1] == ID:
                        result[_line_index] = {
                            "var": {
                                "name": _id[0],
                                "type": _type,
                                "value": {
                                    "id": _value[0]
                                }
                            }
                        }
                    else:
                        _t = 'literal'
                        if _value[0] == 'input':
                            _value = {
                                'input': {
                                    'args': []
                                }
                            }
                            _t = 'function'
                        else:
                            _value = _value[0]
                        result[_line_index] = {
                            "var": {
                                "name": _id[0],
                                "type": _type,
                                "value": {
                                    _t: _value
                                }
                            }
                        }
        
        return result
