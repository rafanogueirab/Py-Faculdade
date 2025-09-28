#def divide(x, y):
    #assert y != 0, "Divisão por Zero!"
    #return x / y
#import sys
#result = divide(6, 2)
#print(result)
#import doctest

#def square(x):
   # """
    #Retorna o quadrado de um número

    #Exemplos:
    #>>> square(3)
    #9
    #>>> square(-2)
    #4
    #>>> square(0)
    #0
    #"""
    #return x * x
#doctest.testmod()

import unittest
def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    print('Os testes foram executados com sucesso.')