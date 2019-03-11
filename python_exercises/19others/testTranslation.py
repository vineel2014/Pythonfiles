import Translation
import unittest

input = 'John eats bread & drinks wine'
output = 'John mange du-pain & bois du-vin'

class TestSaytime(unittest.TestCase):
    def setUp(self):
        self.input = input.split()
        self.result = output.split()
        
    def test(self):        
        
        for i,word in enumerate(self.result):
            self.assertEqual(Translation.translate(self.input[i]), word)
        
        self.assertEqual(Translation.translate(input),output)
        
        

if __name__ == "__main__": unittest.main()
