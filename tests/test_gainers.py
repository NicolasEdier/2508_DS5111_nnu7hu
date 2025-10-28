import unittest
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bin', 'gainers')))

from yahoo import GainerYahoo
from wsj import GainerWSJ

class TestGainerNormalizers(unittest.TestCase):
    
    def test_yahoo_normalize(self):
        """Test Yahoo normalizer produces correct columns"""
        gainer = GainerYahoo()
        
        normalized = gainer.normalize_data()
        
        # Check that all required columns exist
        expected_columns = ['symbol', 'company_name', 'price', 'change', 
                          'perc_change', 'volume']
        self.assertEqual(list(normalized.columns), expected_columns)
        
        # Check that it's not empty
        self.assertGreater(len(normalized), 0)
    
    def test_wsj_normalize(self):
        """Test WSJ normalizer produces correct columns"""
        gainer = GainerWSJ()
        
        normalized = gainer.normalize_data()
        
        # Check that all required columns exist
        expected_columns = ['symbol', 'company_name', 'price', 'change', 
                          'perc_change', 'volume']
        self.assertEqual(list(normalized.columns), expected_columns)
        
        # Check that it's not empty
        self.assertGreater(len(normalized), 0)

if __name__ == '__main__':
    unittest.main()
