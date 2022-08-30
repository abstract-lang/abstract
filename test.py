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

if __name__ == "__main__":
    unittest.main()
