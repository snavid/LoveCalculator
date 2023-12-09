import unittest
from LoveCalculator import NormalLoveCalc, BestLoveCalc
class TestLoveCalculator(unittest.TestCase):
    
    def testNormalLoveCalculator(self):
        self.assertEqual(NormalLoveCalc("Yunus" ,"Angel"), "96%")
    def testBestLoveCalculator(self):
        self.assertEqual(BestLoveCalc("Yun", "Ang"), "74%")
        
if __name__ == "__main__":
    unittest.main()