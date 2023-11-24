# author: Mo Norouzi
# date: 2023-11-24

import pandas as pd
import altair as alt
from numeric_cols import create_numeric_cols_chart 

# Create sample data for testing
def create_sample_data():
    data = {
        "MONTH": [1, 2, 3, 4, 5],
        "DAY": [10, 15, 20, 25, 30],
        "HOUR": [8, 12, 16, 20, 24],
        "MINUTE": [0, 15, 30, 45, 60]
    }
    return pd.DataFrame(data)

def test_create_numeric_cols_chart():
    # Given
    data = create_sample_data()
    numeric_cols = ["MONTH", "DAY", "HOUR", "MINUTE"]

    # When
    result_chart = create_numeric_cols_chart(data, numeric_cols)

    # Then
    assert isinstance(result_chart, alt.Chart)
    assert len(result_chart) == len(numeric_cols)

def test_plotting_numeric_cols():
    # Given
    data = create_sample_data()
    numeric_cols = ["MONTH", "DAY", "HOUR", "MINUTE"]

    # When
    plot = plotting_numeric_cols(data, numeric_cols)

    # Then
    assert isinstance(plot, alt.Chart)
    assert len(plot) == len(numeric_cols)

