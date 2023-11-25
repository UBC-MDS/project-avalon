# author: Mo Norouzi
# date: 2023-11-24

import pandas as pd
import pytest
from missing_value import missing_zero_values_table  

# Create sample data for testing
@pytest.fixture
def sample_data():
    data = {
        "A": [1, 2, 0, 4, 5],
        "B": [0, 5, 0, 8, 9],
        "C": [1, 2, None, 4, 5],
        "D": [1, 2, 3, 4, 5],
        "E": [0, 0, 0, 0, 0]
    }
    return pd.DataFrame(data)

def test_missing_zero_values_table(sample_data, capsys):
    # When
    result_table = missing_zero_values_table(sample_data)

    # Then
    assert isinstance(result_table, pd.DataFrame)
    assert result_table.index.tolist() == ['E', 'B', 'C']
    assert result_table.columns.tolist() == ['Zero Values', 'Missing Values', '% of Total Values', 'Total Zero Missing Values', '% Total Zero Missing Values', 'Data Type']
    assert result_table['Zero Values'].equals(pd.Series([5, 2, 0], index=['E', 'B', 'C']))
    assert result_table['Missing Values'].equals(pd.Series([0, 1, 1], index=['E', 'B', 'C']))
    assert result_table['% of Total Values'].equals(pd.Series([100.0, 20.0, 20.0], index=['E', 'B', 'C']))
    assert result_table['Total Zero Missing Values'].equals(pd.Series([5, 3, 1], index=['E', 'B', 'C']))
    assert result_table['% Total Zero Missing Values'].equals(pd.Series([100.0, 60.0, 20.0], index=['E', 'B', 'C']))
    assert result_table['Data Type'].equals(pd.Series([int, int, float], index=['E', 'B', 'C']))
    
    captured = capsys.readouterr()
    assert "Your selected dataframe has 5 columns and 5 Rows.\nThere are 3 columns that have missing values." in captured.out
