
import unittest

def multiply(a,b):
	return a*b

def add(a,b):
	return a+b

def subtract(a,b):
	return a-b

def divide(a,b):
	return a/b 

class test_calculator(unittest.TestCase):

    def test_sum(self):
    	self.assertEqual(add(2,4),2+4)

    def test_multiply(self):
    	self.assertEqual(multiply(2,4),2*4)

    def test_subtract(self):
    	self.assertEqual(subtract(4,2),4-2)

    def test_divide(self):
    	self.assertEqual(divide(4,2),4/2)

if __name__ == '__main__':
    unittest.main()