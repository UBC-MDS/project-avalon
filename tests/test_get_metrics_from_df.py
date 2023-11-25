# author: Yiwei Zhang
# date: 2023-11-24
import pandas as pd
import pytest
import sys
sys.path.append('../src/helpers')
from get_metrics_from_df import get_metrics_from_df


def test_non_dataframe_input():
    # Given: A non-DataFrame input
    df = 'not a dataframe'
    target_column = 'Actual'
    required_metrics = ['mae', 'mse']

    # Then: Expect a TypeError
    with pytest.raises(TypeError):
        get_metrics_from_df(df, target_column, required_metrics)

# Test for Handling Unsupported Metrics


def test_unsupported_metric():
    # Given: A normal DataFrame and an unsupported metric
    data = {'Actual': [1, 2, 3], 'Forecast': [1, 2, 3]}
    df = pd.DataFrame(data)
    target_column = 'Actual'
    required_metrics = ['unsupported_metric']

    # When: Calling the function
    result = get_metrics_from_df(df, target_column, required_metrics)

    # Then: Verify that the unsupported metric is ignored or handled properly
    assert all(metric not in result.columns for metric in required_metrics)

# Test for Handling Empty DataFrame


def test_empty_dataframe():
    # Given: An empty DataFrame
    df = pd.DataFrame()
    target_column = 'Actual'
    required_metrics = ['mae', 'mse']

    # Then: Expect an appropriate error or handling mechanism
    with pytest.raises(ValueError):
        get_metrics_from_df(df, target_column, required_metrics)

# Test for Correct Handling of Missing Target Column


def test_missing_target_column():
    # Given: A DataFrame without the specified target column
    data = {'Forecast': [1, 2, 3]}
    df = pd.DataFrame(data)
    target_column = 'Actual'
    required_metrics = ['mae', 'mse']

    # Then: Expect an appropriate error or handling mechanism
    with pytest.raises(KeyError):
        get_metrics_from_df(df, target_column, required_metrics)
