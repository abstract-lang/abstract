from typing import TypeAlias
from lexpl import lex
from parsepl import Parser


FileName: TypeAlias = str
FileData: TypeAlias = str


class EnterToAbstr:
    def _get_characters(self, filename: FileName) -> FileData:
        with open(filename, mode='r', encoding='utf-8') as file:
            return file.read()

    def run(self, filename: FileName):
        characters = self._get_characters(filename)
        tokens = lex(characters)
        parser = Parser()
        parser.parse(tokens)
