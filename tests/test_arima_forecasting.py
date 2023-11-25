import pytest
import pandas as pd
import numpy as np
import sys
import os

# Import the count_classes function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.arima_forecasting import arima_prediction

# Test Data
data = np.random.rand(50, 1)  # Generating random data
sample_df = pd.DataFrame(data, columns=['Value'], index=pd.date_range('2023-01-01', periods=50, freq='D'))
two_col_df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
non_datetime_index_df = pd.DataFrame({'Values': [1, 2, 3]}, index=[1, 2, 3])
non_numeric_df = pd.DataFrame({'Values': ['a', 'b', 'c']}, index=pd.date_range('2023-01-01', periods=3, freq='D'))

# Function to test if the output length matches the expected length
def test_output_length():
    forecasted_values = arima_prediction(sample_df, window_size=12)
    assert len(forecasted_values) == len(sample_df) - 12 + 1, "The output length does not match the expected length"

# Function to test if the output values are numeric
def test_output_values():
    forecasted_values = arima_prediction(sample_df, window_size=12)
    assert all(isinstance(val, (int, float)) for val in forecasted_values), "The predicted values should be numeric"

# Test for multiple columns in the DataFrame
def test_invalid_column_count():
    with pytest.raises(ValueError):
        arima_prediction(two_col_df)

# Test for non-DatetimeIndex index
def test_non_datetime_index():
    with pytest.raises(ValueError):
        arima_prediction(non_datetime_index_df)

# Test for non-numeric column
def test_non_numerical_column():
    with pytest.raises(ValueError):
        arima_prediction(non_numeric_df)

# Test for invalid window size
def test_invalid_window_size():
    with pytest.raises(ValueError):
        arima_prediction(sample_df, window_size=0)