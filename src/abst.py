import sys
from lexer import lex_pl
from astcrearor import ASTcreator
from runner import Runner

if __name__ == '__main__':
    filename = sys.argv[1]
    
    file = open(filename, encoding="utf-8")
    characters = file.read()
    
    characters += "\n"  # For fix error with ignoring last line
    
    file.close()
    token_lines = lex_pl(characters)

    ast_creator = ASTcreator(token_lines)
    
    builded_ast = ast_creator.build()
    
    # print(builded_ast)
    
    runner = Runner(builded_ast)
    
    runner.run()
