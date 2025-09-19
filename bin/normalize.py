#!/usr/bin/env python3
"""
Stock data normalizer for Yahoo Finance and Wall Street Journal CSV files.
"""

import pandas as pd
import re


def normalize_yahoo(csv_path):
    """
    Normalize Yahoo Finance gainers CSV to standard format.
    """
    df = pd.read_csv(csv_path)
    
    normalized = pd.DataFrame({
        'symbol': df['Symbol'],
        'company_name': df['Name'],
        'price': df['Price'].apply(lambda x: str(x).split()[0]),
        'change': df['Change'],
        'perc_change': df['Change %'].apply(lambda x: str(x).replace('+', '').replace('%', '')),
        'volume': df['Volume']
    })
    
    return normalized


def normalize_wsj(csv_path):
    """
    Normalize Wall Street Journal gainers CSV to standard format.
    """
    df = pd.read_csv(csv_path)
    
    # Extract symbol from "Company Name (SYMBOL)" format
    rex = r'\(([A-Z]+)\)$'
    
    normalized = pd.DataFrame({
        'symbol': df['Unnamed: 0'].apply(lambda x: re.findall(rex, str(x))[0] if re.findall(rex, str(x)) else ''),
        'company_name': df['Unnamed: 0'].apply(lambda x: re.sub(r'\s*\([A-Z]+\)$', '', str(x)).strip()),
        'price': df['Last'],
        'change': df['Chg'],
        'perc_change': df['% Chg'],
        'volume': df['Volume']
    })
    
    return normalized


if __name__ == "__main__":
    # Test the functions
    try:
        yahoo_df = normalize_yahoo('../ygainers.csv')
        wsj_df = normalize_wsj('../wsjgainers.csv')
        
        print("Yahoo sample:")
        print(yahoo_df.head())
        print("\nWSJ sample:")
        print(wsj_df.head())
        
        # Save normalized files
        yahoo_df.to_csv('normalized_yahoo.csv', index=False)
        wsj_df.to_csv('normalized_wsj.csv', index=False)
        
    except FileNotFoundError as e:
        print(f"File not found: {e}")
