# author: Mo Norouzi
# date: 2023-11-24

import pandas as pd
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from src.missing_value import missing_zero_values_table  

# Create sample data for testing
@pytest.fixture
def sample_data():
    data = {
        "A": [1, 2, 3, 4, 5],
        "B": [0, None, 0, 8, 9],
        "C": [1, 2, None, 4, 5],
        "D": [1, 2, 3, 4, 5],
        "E": [0, 0, 0, 0, None]
    }
    return pd.DataFrame(data)

def test_missing_zero_values_table(sample_data, capsys):
    # When
    result_table = missing_zero_values_table(sample_data)

    # Then
    assert isinstance(result_table, pd.DataFrame)
    assert result_table.index.tolist() == ['B', 'C', 'E']
    assert result_table.columns.tolist() == ['Zero Values', 'Missing Values', '% of Total Values', 'Total Zero Missing Values', '% Total Zero Missing Values', 'Data Type']
    assert result_table['Zero Values'].equals(pd.Series([2, 0, 4], index=['B', 'C', 'E']))
    assert result_table['Missing Values'].equals(pd.Series([1, 1, 1], index=['B', 'C', 'E']))
    assert result_table['% of Total Values'].equals(pd.Series([20.0, 20.0, 20.0], index=['B', 'C', 'E']))
    assert result_table['Total Zero Missing Values'].equals(pd.Series([3, 1, 5], index=['B', 'C', 'E']))
    assert result_table['% Total Zero Missing Values'].equals(pd.Series([60.0, 20.0, 100.0], index=['B', 'C', 'E']))
    assert result_table['Data Type'].equals(pd.Series([float, float, float], index=['B', 'C', 'E']))
    
    captured = capsys.readouterr()
    assert "Your selected dataframe has 5 columns and 5 Rows.\nThere are 3 columns that have missing values." in captured.out
