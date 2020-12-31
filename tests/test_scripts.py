import pytest
import os

def test_conversion():
    if os.path.exists('temperature.db'):
        os.remove('temperature.db')

    with open('scripts/convert_csv_to_sql.py','r') as f:
        exec(f.read())
    
    assert os.path.exists('temperature.db')