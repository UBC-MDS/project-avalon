import pytest
import pandas as pd
import numpy as np
from src/arima_forecasting import arima_prediction  

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

# # Test for multiple columns in the DataFrame
# def test_invalid_column_count():
#     try:
#         arima_prediction(two_col_df)
#     except ValueError as e:
#         assert str(e) == "Input DataFrame must contain only one column for ARIMA prediction."

# # Test for non-DatetimeIndex index
# def test_non_datetime_index():
#     try:
#         arima_prediction(non_datetime_index_df)
#     except ValueError as e:
#         assert str(e) == "Index of the DataFrame must be a DatetimeIndex for ARIMA prediction."

# # Test for non-numeric column
# def test_non_numerical_column():
#     try:
#         arima_prediction(non_numeric_df)
#     except ValueError as e:
#         assert str(e) == "The column in the DataFrame should be numerical for ARIMA prediction."

# # Test for invalid window size
# def test_invalid_window_size():
#     try:
#         arima_prediction(sample_df, window_size=0)
#     except ValueError as e:
#         assert str(e) == "Window size must be a positive integer that is greater than 1 and less than the length of df for ARIMA prediction."