import sys

class BaseException_:
    __exname__: str
    def __raise__(self, text: str):
        print(
            f'{self.__exname__}: {text}\n',
            sep='\n'
        )
        sys.exit(1)

class LexerError_(BaseException_):
    __exname__ = 'LexerError'

class NameError_(BaseException_):
    __exname__ = 'NameError'

class SyntaxError_(BaseException_):
    __exname__ = 'SyntaxError'
