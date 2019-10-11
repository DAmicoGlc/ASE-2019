import calculator as c
import unittest
 
class TestGcd(unittest.TestCase):
 
    def test_gcd_integers(self):
        result = c.gcd(6, 3)
        self.assertEqual(result, 3)
    
    def test_gcd_integers2(self):
        result = c.gcd(36, 12)
        self.assertEqual(result, 12)

    def test_gcd_integers3(self):
        result = c.gcd(48, 32)
        self.assertEqual(result, 16)    
    
    def test_gcd_integers4(self):
        result = c.gcd(33, 22)
        self.assertEqual(result, 11)

    def test_gcd_zero_integers(self):
        result = c.gcd(0, 22)
        self.assertEqual(result, 22)
    
    def test_gcd_zero_integers2(self):
        result = c.gcd(11, 0)
        self.assertEqual(result, 11)

    def test_gcd_integers_negative(self):
       self.assertRaises(ValueError, c.gcd, -6, 3)

    def test_gcd_integers_negative(self):
       self.assertRaises(ValueError, c.gcd, 6, -3)
        

if __name__ == '__main__':
    unittest.main()