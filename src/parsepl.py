from asts import Function, Signature, Argument, Type, ASTobject
from local_names import PrintFunction
from exceptions.base import NameError_, SyntaxError_

class _SerializeLiteral:
    def __new__(cls, _token: tuple[str, str]) -> None:
        token, tag = _token
        
        if tag == 'STR_LITERAL':
            return token.replace("'" if token.startswith("'") else '"', '', 2)
        if tag == 'INT_LITERAL':
            return int(token)
        return token

class Parser:
    locals_: dict[str, ASTobject] = {
        'str': Type('str'),
        'any': Type('any'),
        'print': PrintFunction(
            signature=Signature(
                Argument('arg', 'any'),
                rtype='any'
            ),
        ),
    }
    
    def _resolve_arguments(self, tokens_in_brackets: list[tuple[str, str]]):
        print(f'{tokens_in_brackets=}')
        
        args, kwargs = [], {}
        
        for pos, (token, tag) in enumerate(tokens_in_brackets):
            if tag == 'COMMA':
                try:
                    if tokens_in_brackets[pos - 2][1] == 'ASSIGN':
                        name = tokens_in_brackets[pos - 3][0]
                        value = _SerializeLiteral(tokens_in_brackets[pos - 1])
                        kwargs[name] = value
                    else:
                        arg = _SerializeLiteral(tokens_in_brackets[pos - 1])
                        args.append(arg)
                except IndexError:
                    arg = _SerializeLiteral(tokens_in_brackets[pos - 1])
                    args.append(arg)

        print(f'{args=} {kwargs=}')
        return args, kwargs

    def parse(self, tokens: list[tuple[str, str]]):
        _t = tokens.copy()
        for pos, (token, tag) in enumerate(_t):
            if tag == 'SPACE':
                try:
                    tokens.remove( (token, tag) )
                except ValueError:
                    break
        del _t
        print(tokens)
        __t = tokens.copy()
        
        for i, _ in enumerate(__t):
            pos = i
            try:
                token, tag = tokens[i]
            except IndexError:
                continue
            if tag == 'NAME':
                try:
                    object = self.locals_[token]
                    open_bracket_index = pos + 1
                    close_bracket_index = tokens.index((')', 'ROUND_BRACKET_CLOSE'), pos + 1)
                    if tokens[open_bracket_index] != ('(', 'ROUND_BRACKET_OPEN'):
                        SyntaxError_().__raise__('After method name you must type "(" character!')

                    tokens_in_brackets = tokens[open_bracket_index+1:close_bracket_index]
                    print(f'{open_bracket_index=}\n{close_bracket_index=}')
                    args, kwargs = self._resolve_arguments(tokens_in_brackets)
                    
                    object._eval_(*args, **kwargs)
                    
                    del tokens[pos:close_bracket_index]
                except KeyError:
                    NameError_().__raise__(f'Invalid name: {token}')
        