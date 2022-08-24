import lexer

RESERVED = 'RESERVED'
FUNCTION = 'FUNCTION'
TYPE     = 'TYPE'
INT      = 'INT'
STR      = 'STRING'
ID       = 'ID'
FLOAT    = 'FLOAT'
BOOL     = 'BOOLEAN'
NEW_LINE = "NEW_LINE"

token_exprs = [
    (r';',                 NEW_LINE),
    (r'[ \n\t]+',              None),
    (r'#\s*[^\n]*',            None),
    (r' +',                    None),
    (r'\(',                RESERVED),
    (r'\)',                RESERVED),
    (r'\+',                RESERVED),
    (r'\-',                RESERVED),
    (r'\*',                RESERVED),
    (r'\/',                RESERVED),
    (r'\,',                RESERVED),
    (r'print',             FUNCTION),
    (r'input',             RESERVED),
    (r'int',                   TYPE),
    (r'str',                   TYPE),
    (r'bool',                  TYPE),
    (r'flo',                   TYPE),
    (r'true',                  BOOL),
    (r'false',                 BOOL),
    (r'\d{1,}.\d{1,}',        FLOAT),
    (r'"[^\n]{0,}"',            STR),
    (r"'[^\n]{0,}'",            STR),
    (r'=',                 RESERVED),
    (r'[0-9]+',                 INT),
    (r'[A-Za-z][A-Za-z0-9_]*',   ID)
]

def i_lex(characters):
    resources = lexer.lex(characters, token_exprs)
    result = []

    last_new_line = 0
    
    for i in resources:
        if i[1] == NEW_LINE:
            _list = resources[last_new_line:resources.index(i, last_new_line + 1)]
            
            for _iter in range(len(_list)):
                try:
                    _list.remove((';', NEW_LINE))
                except ValueError:
                    pass
            
            result.append(_list)
            
            last_new_line = resources.index(i, last_new_line + 1)

    for _iter in range(len(result)):
        try:
            result.remove([])
        except ValueError:
            pass

    return result
