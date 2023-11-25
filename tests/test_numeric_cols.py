# author: Mo Norouzi
# date: 2023-11-24

import pandas as pd
import altair as alt
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__),".."))

from src.numeric_cols import create_numeric_cols_chart 

# Sample test data
data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9],
    'D': ['a', 'b', 'c']
})

def test_create_numeric_cols_chart_output_type():
    # Test if the output is of type alt.Chart
    result_chart = create_numeric_cols_chart(data, ['A', 'B', 'C'])
    assert isinstance(result_chart, alt.vegalite.v5.api.HConcatChart)


def test_create_numeric_cols_chart_empty_columns():
    # Test if the function handles an empty list of columns
    result_chart = create_numeric_cols_chart(data, [])
    assert isinstance(result_chart, alt.vegalite.v5.api.HConcatChart)

def test_create_numeric_cols_chart_numeric():
    try:
        pd.to_numeric(data, ['A', 'B', 'D'])
    except Exception as e:
        assert isinstance(e, ValueError)




