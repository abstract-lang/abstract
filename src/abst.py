import sys
from lexpl import lex_pl, lex
from parse import Parser
from runner import Runner

if __name__ == '__main__':
    filename = sys.argv[1]
    
    file = open(filename, encoding="utf-8")
    characters = file.read()
    
    characters += "\n"  # For fix error with ignoring last line
    
    file.close()
    
    resources = lex(characters)
    print(resources)
    token_lines = lex_pl(resources)
    
    print(token_lines)
    
    parsed = Parser(resources, token_lines).parse()
    
    Runner(parsed).run()
