import re

from exceptions.base import LexerError_

token_exprs = (
    (r' +',          'SPACE'),
    (r'\n',         'NEW_FILE'),
    (r'    ',       'INDENT'),
    (r',',          'COMMA'),
    (r'=',          'ASSIGN'),
    # Literals      #
    (r"'[^\n']*'",   'STR_LITERAL'),
    (r'"[^\n"]*"',   'STR_LITERAL'),
    (r'[0-9]+',      'INT_LITERAL'),
    #               #
    (r'\w+',        'NAME'),
    (r'[(]',        'ROUND_BRACKET_OPEN'),
    (r'[)]',        'ROUND_BRACKET_CLOSE'),
)

def lex(characters):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match and tag:
                tokens.append( (match.group(0), tag) )
                break
        if not match:
            LexerError_().__raise__(f'Invalid character: "{characters[pos]}"')
        else:
            pos = match.end(0)
    return tokens
