import sys
import os
import pandas as pd
import pytest
from io import StringIO

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.capture_df_info import capture_df_info

# Test for capture_df_info
def test_capture_df_info():
    # Create a sample DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    df = pd.DataFrame(data)

    # Use the capture_df_info function to get the DataFrame info as a string
    df_info_string = capture_df_info(df)

    # Expected output
    expected_start = "<class 'pandas.core.frame.DataFrame'>"
    expected_columns = "Data columns (total 3 columns):"

    # Check if the function output starts with the expected string
    assert df_info_string.startswith(expected_start)
    assert expected_columns in df_info_string
    # Ensure that the info string contains the column names
    for column in data.keys():
        assert column in df_info_string
