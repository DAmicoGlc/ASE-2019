import calculator as c
import unittest
 
class TestPerc(unittest.TestCase):
 
    def test_percentage_integers(self):
        result = c.percentage(100, 20)
        self.assertEqual(result, 20)

    def test_percentage_integers2(self):
        result = c.percentage(140, 200)
        self.assertEqual(result, 280)    

    def test_percentage_integers3(self):
        result = c.percentage(250, 50)
        self.assertEqual(result, 125)  

    def test_percentage_integers4(self):
        result = c.percentage(200, 0.5)
        self.assertEqual(result, 1)

    def test_percentage_integers4(self):
        result = c.percentage(200, 0.5)
        self.assertEqual(result, 1)

    def test_percentage_zero_integers(self):
        result = c.percentage(0, 50)
        self.assertEqual(result, 0)
    
    def test_percentage_zero_integers2(self):
        result = c.percentage(110, 0)
        self.assertEqual(result, 0)

    def test_percentage_integers_negative(self):
       self.assertRaises(ValueError, c.percentage, -6, 3)

    def test_percentage_integers_negative(self):
       self.assertRaises(ValueError, c.percentage, 6, -3)  
 
 
if __name__ == '__main__':
    unittest.main()