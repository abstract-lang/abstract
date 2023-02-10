from asts import Function

def _get_string_for_print(*args, sep: str = ' '):
    _str = ''
    for i in args:
        _str += (i + sep)
    _str = _str.removesuffix(sep)
    return _str

class PrintFunction(Function):
    def _eval_(self, *args, sep: str = ' '):
        x = _get_string_for_print(*args, sep=sep)
        print(x)
        return x
