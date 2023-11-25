import sys
import os
import pytest

import pandas as pd
import numpy as np


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.correlation import get_top_abs_correlations, get_redundant_pairs


# Tests for get_redundant_pairs
# Test case 1: Valid DataFrame
def test_get_redundant_pairs_valid_df():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    df = pd.DataFrame(data)
    result = get_redundant_pairs(df)
    expected = {('A', 'A'), ('B', 'B'), ('C', 'C'), ('B', 'A'), ('C', 'A'), ('C', 'B')}
    assert result == expected


# Test case 2: Invalid input type (non-DataFrame)
def test_get_redundant_pairs_invalid_input_type():
    with pytest.raises(TypeError):
        get_redundant_pairs("not_a_dataframe")


# Test case 3: Empty DataFrame
def test_get_redundant_pairs_empty_df():
    empty_df = pd.DataFrame()
    result = get_redundant_pairs(empty_df)
    assert result == set()


# Tests for get_top_abs_correlations
# Test case 1: Valid input DataFrame
def test_valid_input():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    result = get_top_abs_correlations(df, n=2)
    assert isinstance(result, pd.Series)
    assert len(result) == 1


# Test case 2: Non-pandas DataFrame input
def test_non_dataframe_input():
    with pytest.raises(TypeError):
        get_top_abs_correlations(np.array([1, 2, 3]))


# Test case 3: Correct exclusion of redundant pairs
def test_redundant_pairs_exclusion():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9],
        'D': [10, 11, 12]
    })

    redundant_pairs = get_redundant_pairs(df)
    assert len(redundant_pairs) == 10
    result = get_top_abs_correlations(df, n=3)
    assert len(result) == 3
    assert isinstance(result, pd.Series)

