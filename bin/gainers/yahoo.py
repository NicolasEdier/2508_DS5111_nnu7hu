import os
import pandas as pd
from base import GainerBase

class GainerYahoo(GainerBase):
    def __init__(self):
        pass
    
    def download_html(self):
        print("Yahoo download html")
        os.system("sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html")
    
    def extract_csv(self):
        print("Yahoo create csv")
        raw = pd.read_html('ygainers.html')
        raw[0].to_csv('ygainers.csv')
    
    def normalize_data(self):
        print("Yahoo normalize csv")
        """
        Normalize Yahoo Finance gainers CSV to standard format.
        """
        df = pd.read_csv('ygainers.csv')
        normalized = pd.DataFrame({
            'symbol': df['Symbol'],
            'company_name': df['Name'],
            'price': df['Price'].apply(lambda x: str(x).split()[0]),
            'change': df['Change'],
            'perc_change': df['Change %'].apply(
                lambda x: str(x).replace('+', '').replace('%', '')
            ),
            'volume': df['Volume']
        })
        return normalized


if __name__=="__main__":
    import sys
    assert len(sys.argv) == 2, "Please pass in one of 'html', 'csv', 'normalize'"
    function = sys.argv[1]
    valid_functions = ['html', 'csv', 'normalize']
    assert function in valid_functions, f"Expected one of {valid_functions} but got {function}"
    
    gainer = GainerYahoo()
    
    if function == 'html':
        gainer.download_html()
    elif function == 'csv':
        gainer.extract_csv()
    elif function == 'normalize':
        gainer.normalize_data()
