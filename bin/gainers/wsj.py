import os
import re
import pandas as pd
from base import GainerBase

class GainerWSJ(GainerBase):
    def __init__(self):
        pass
    
    def download_html(self):
        print("WSJ download html")
        os.system("sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 https://www.wsj.com/market-data/stocks/us/movers > wsjgainers.html")
    
    def extract_csv(self):
        print("WSJ create csv")
        raw = pd.read_html('wsjgainers.html')
        raw[0].to_csv('wsjgainers.csv')
    
    def normalize_data(self):
        print("WSJ normalize csv")
        """
        Normalize Wall Street Journal gainers CSV to standard format.
        """
        df = pd.read_csv('wsjgainers.csv')
        # Extract symbol from "Company Name (SYMBOL)" format
        rex = r'\(([A-Z]+)\)$'
        normalized = pd.DataFrame({
            'symbol': df['Unnamed: 0'].apply(
                lambda x: re.findall(rex, str(x))[0] if re.findall(rex, str(x)) else ''
            ),
            'company_name': df['Unnamed: 0'].apply(
                lambda x: re.sub(r'\s*\([A-Z]+\)$', '', str(x)).strip()
            ),
            'price': df['Last'],
            'change': df['Chg'],
            'perc_change': df['% Chg'],
            'volume': df['Volume']
        })
        return normalized


if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2, "Please pass in one of 'html', 'csv', 'normalize'"
    function = sys.argv[1]
    valid_functions = ['html', 'csv', 'normalize']
    assert function in valid_functions, f"Expected one of {valid_functions} but got {function}"
    
    gainer = GainerWSJ()
    
    if function == 'html':
        gainer.download_html()
    elif function == 'csv':
        gainer.extract_csv()
    elif function == 'normalize':
        gainer.normalize_data()
