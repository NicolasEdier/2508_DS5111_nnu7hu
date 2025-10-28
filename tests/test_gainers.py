import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bin', 'gainers')))

from yahoo import GainerYahoo
from wsj import GainerWSJ

def test_python_version():
    assert sys.version_info.major == 3
    assert sys.version_info.minor in [12, 13]

def test_yahoo_class_exists():
    """Test that Yahoo class can be instantiated"""
    gainer = GainerYahoo()
    assert gainer is not None
    assert hasattr(gainer, 'download_html')
    assert hasattr(gainer, 'extract_csv')
    assert hasattr(gainer, 'normalize_data')

def test_wsj_class_exists():
    """Test that WSJ class can be instantiated"""
    gainer = GainerWSJ()
    assert gainer is not None
    assert hasattr(gainer, 'download_html')
    assert hasattr(gainer, 'extract_csv')
    assert hasattr(gainer, 'normalize_data')
