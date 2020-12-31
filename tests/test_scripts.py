import pytest
import os
import scripts.convert_csv_to_sql

def test_conversion():
    if os.path.exists('temperature.db'):
        os.remove('temperature.db')
    scripts.convert_csv_to_sql.process(csv_name='data/temperature.csv')
    assert os.path.exists('temperature.db')