import sys
import re

RESERVED        = 'RESERVED'
FUNCTION        = 'FUNCTION'
TYPE            = 'TYPE'
INT             = 'INT'
STR             = 'STRING'
ID              = 'ID'
FLOAT           = 'FLOAT'
BOOL            = 'BOOLEAN'
NEW_LINE        = 'NEW_LINE'
IF_ELSE         = 'IF_ELSE'
STATEMENT_OPEN  = 'STATEMENT_OPEN'
STATEMENT_CLOSE = 'STATEMENT_CLOSE'
MATH_OPERATION  = 'MATH_OPERATION'

token_exprs = [
    (r'\n',                 NEW_LINE),
    (r'[ \n\t]+',              None),
    (r'#\s*[^\n]*',            None),
    (r'==',          MATH_OPERATION),
    (r'=',                 RESERVED),
    (r'\(',                RESERVED),
    (r'\)',                RESERVED),
    (r'\+',          MATH_OPERATION),
    (r'\-',          MATH_OPERATION),
    (r'\*',          MATH_OPERATION),
    (r'\/',          MATH_OPERATION),
    (r'\,',                RESERVED),
    (r'{',           STATEMENT_OPEN),
    (r'}',          STATEMENT_CLOSE),
    (r'if',                 IF_ELSE),
    (r'print',             FUNCTION),
    (r'input',             RESERVED),
    (r'int',                   TYPE),
    (r'str',                   TYPE),
    (r'bool',                  TYPE),
    (r'flo',                   TYPE),
    (r'true',                  BOOL),
    (r'false',                 BOOL),
    (r'[0-9]+\.[0-9]+',       FLOAT),
    (r'"[^\n]{0,}"',            STR),
    (r"'[^\n]{0,}'",            STR),
    (r'[0-9]+',                 INT),
    (r'[A-Za-z][A-Za-z0-9_]*',   ID)
]

def lex(characters):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens

def lex_pl(resources):
    result = []

    last_new_line = 0
    
    for i in resources:
        if i[1] == NEW_LINE:
            _list = resources[last_new_line:resources.index(i, last_new_line + 1)]
            
            for _iter in range(len(_list)):
                try:
                    _list.remove(('\n', NEW_LINE))
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