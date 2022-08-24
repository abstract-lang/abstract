class Runner:
    def __init__(self, builded_ast: dict) -> None:
        self.ast = builded_ast
        
        self.variables = {}
        self.functions = {}
    
    def run(self):
        for i in self.ast.items():
            _json = i[1]
            
            try:
                _op = list(_json.keys())[0]
                
                if _op == "var":
                    _var = _json[_op]
                    _value = ""
                    _type = _var["type"]
                    
                    _value_json = _var["value"]
                    
                    _value_index_in_var = list(_value_json.keys())[0]
                    
                    if _value_index_in_var == "literal":
                        _value = _value_json[_value_index_in_var]
                        
                        if _type == "str":
                            if str(_value).startswith('"'):
                                _value = _value.replace('"', '')
                            elif str(_value).startswith("'"):
                                _value = _value.replace("'", '')
                            else:
                                raise TypeError("Invalid literal of string object!")
                    
                    elif _value_index_in_var == "id":
                        _value_json = _var["value"]
                        
                        _id = _value_json[_value_index_in_var]
                        
                        _value = self.variables[_id]
                    
                    elif _value_index_in_var == "function":
                        _value_json = _var["value"]
                        _func_json = _value_json[_value_index_in_var]
                        
                        _func_name = list(_func_json)[0]
                        
                        if _func_name == "input":
                            _value = input()
                    
                    self.variables.setdefault(_var["name"], _value)

                if _op == "print":
                    _print = _json[_op]
                    
                    _args = _print["args"]
                    
                    for arg in _args:
                        if list(arg.keys())[0] == "id":
                            print(self.variables[arg["id"]])
                        if list(arg.keys())[0] == "literal":
                            _literal_json = arg["literal"]
                            
                            _type = _literal_json["type"]
                            _value = _literal_json["value"]
                            
                            if _type == "string":
                                if str(_value).startswith('"'):
                                    _value = _value.replace('"', '')
                                elif str(_value).startswith("'"):
                                    _value = _value.replace("'", '')
                                else:
                                    raise TypeError("Invalid literal of string object!")
                        
                            print(_value)
            except AttributeError:
                pass
