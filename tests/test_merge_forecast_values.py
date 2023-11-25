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
invalid_df = pd.DataFrame({'Values': ["a", "b", "c", "d"]}, index=pd.date_range('2023-01-01', periods=4))
non_datetime_index_df = pd.DataFrame({'Values': [1, 2, 3]}, index=[1, 2, 3])
sample_forecasted_values = [5, 6]
non_numeric_forecasted_values = [5, '6']
twod_forecasted_values = [[1], [2]]
long_forecasted_values = [1, 2, 3, 4, 5]
sample_col_name = 'Forecasted'
invalid_col_name = 123

# Test whether the output of the function is correct
def test_merge_forecast_values_numeric():
    merged_df = merge_forecast_values(sample_df, sample_forecasted_values, sample_col_name)

    # Check whether output is a dataframe
    assert isinstance(merged_df, pd.DataFrame)
    # Check if a new column is added
    assert sample_col_name in merged_df.columns
    # Check whether output has correct length
    assert len(merged_df) == len(sample_df) + 1
    # Check whether index of output is DatetimeIndex
    assert isinstance(merged_df.index, pd.DatetimeIndex)

# Test for non-DatetimeIndex df
def test_merge_forecast_values_non_datetime_index_df():
    with pytest.raises(ValueError):
        merge_forecast_values(non_datetime_index_df, sample_forecasted_values, sample_col_name)

# Test for non-numerical df as first column
def test_merge_forecast_values_invalid_df():
    with pytest.raises(ValueError):
        merge_forecast_values(invalid_df, sample_forecasted_values, sample_col_name)

# Test for invalid column name
def test_merge_forecast_values_invalid_col_name():
    with pytest.raises(ValueError):
        merge_forecast_values(sample_df, sample_forecasted_values, invalid_col_name)

# Test for invalid forecasted_values
def test_merge_forecast_values_invalid_values():
    with pytest.raises(ValueError):
        merge_forecast_values(sample_df, non_numeric_forecasted_values, sample_col_name)

# Test for forecasted values that are too long
def test_merge_forecast_values_long_forecasted_values():
    with pytest.raises(ValueError):
        merge_forecast_values(sample_df, long_forecasted_values, sample_col_name)

# Test for 2d forecasted list
def test_merge_forecast_values_2d_list():
    with pytest.raises(ValueError):
        merge_forecast_values(sample_df, twod_forecasted_values, sample_col_name)



