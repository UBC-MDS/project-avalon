import pytest
import pandas as pd
import numpy as np
import sys
import os

# Import the count_classes function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.merge_forecast_values import merge_forecast_values

# Test Data
sample_df = pd.DataFrame({'Values': [1, 2, 3, 4]}, index=pd.date_range('2023-01-01', periods=4))
sample_forecasted_values = [5, 6]
non_numeric_forecasted_values = [5, '6']
sample_col_name = 'Forecasted'
invalid_col_name = 123

def test_merge_forecast_values_numeric():
    merged_df = merge_forecast_values(sample_df, sample_forecasted_values, sample_col_name)
    assert col_name in merged_df.columns
    assert len(merged_df) == len(original_df) + 1

def test_merge_forecast_values_invalid_col_name():
    with pytest.raises(ValueError):
        merge_forecast_values(sample_df, sample_forecasted_values, invalid_col_name)

def test_merge_forecast_values_invalid_values():
    with pytest.raises(ValueError):
        merge_forecast_values(sample_df, non_numeric_forecasted_values, sample_col_name)

