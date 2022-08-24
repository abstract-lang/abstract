import sys
from abst_lexer import i_lex
from abst_parser import ASTcreator
from abst_runner import Runner

if __name__ == '__main__':
    filename = sys.argv[1]
    
    if not filename.endswith('.abst') or not filename.endswith('.abstract'):
        raise RuntimeError("Filename must ends .abst or .abstract string!")
    
    file = open(filename, encoding="utf-8")
    characters = file.read()
    
    characters += "\n"  # For fix error with ignoring last line
    
    file.close()
    token_lines = i_lex(characters)

    ast_creator = ASTcreator(token_lines)
    
    builded_ast = ast_creator.build()
    
    # print(builded_ast)
    
    runner = Runner(builded_ast)
    
    runner.run()
