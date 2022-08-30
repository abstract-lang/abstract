import unittest
from src import lex

class TokenizeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(lex(""), [])
    
    def test_string(self):
        self.assertEqual(lex("'test'"), [("'test'", 'STRING')])
        self.assertEqual(lex('"test"'), [('"test"', 'STRING')])
    
    def test_int(self):
        self.assertEqual(lex('1234'), [('1234', 'INT')])
    
    def test_float(self):
        self.assertEqual(lex('12.34'), [('12.34', 'FLOAT')])
    
    def test_bool(self):
        self.assertEqual(lex('true'), [('true', 'BOOLEAN')])
        self.assertEqual(lex('false'), [('false', 'BOOLEAN')])
    
    def test_print(self):
        self.assertEqual(lex('print()'), [('print', 'FUNCTION'), ('(', 'RESERVED'), (')', 'RESERVED')])
    
    def test_id(self):
        self.assertEqual(lex('abc'), [('abc', 'ID')])
    
    def test_types(self):
        self.assertEqual(lex('str'), [('str', 'TYPE')])
        self.assertEqual(lex('int'), [('int', 'TYPE')])
        self.assertEqual(lex('flo'), [('flo', 'TYPE')])
        self.assertEqual(lex('bool'), [('bool', 'TYPE')])

    def test_var(self):
        self.assertEqual(lex('int abc = 34'), [('int', 'TYPE'), ('abc', 'ID'), ('=', 'RESERVED'), ('34', 'INT')])

if __name__ == "__main__":
    unittest.main()
