import pandas as pd

def merge_forecast_values(original_df, forecasted_values, col_name):
    """
    Merges forecasted values into the original DataFrame with a new column.

    Parameters:
    ----------
    original_df : pandas.DataFrame
        The original DataFrame with historical data.
    forecasted_values : list
        The list of forecasted values to merge.
    col_name : str
        The name for the column containing the forecasted values.

    Returns:
    -------
    pandas.DataFrame
        The original DataFrame with a new column for the forecasted values.

    This function appends the forecasted values to the original DataFrame based on the inferred frequency of the index.
    """

    # Check if the index of original df is a DatetimeIndex
    if not isinstance(original_df.index, pd.DatetimeIndex):
        raise ValueError("Index of the DataFrame must be a DatetimeIndex for ARIMA prediction.")
    
    # Check if all columns in original df is numerical
    if not all(pd.api.types.is_numeric_dtype(original_df.loc[:, col]) for col in original_df.columns):
        raise ValueError("Not all columns in merged_df are numerical.")
    
    # Check if forecasted_values is a 1d list
    if not isinstance(forecasted_values, list) or isinstance(forecasted_values[0], list):
        raise ValueError("Forecasted values must be a 1D list.")
    
    # Check if forecasted_values is a numerical list
    if not all(isinstance(value, (int, float)) for value in forecasted_values):
        raise ValueError("Forecasted values must be a numerical list.")

    # Check if the length of forecasted_values doesn't exceed len(original_df)
    if len(forecasted_values) > len(original_df):
        raise ValueError("Length of forecasted values exceeds the length of the original DataFrame.")
    
    # Check if col_name is a string
    if not isinstance(col_name, str):
        raise ValueError("Column name should be a string.")

    index_freq = original_df.index.inferred_freq
    next_date = pd.Timestamp(original_df.index[-1]) + pd.tseries.frequencies.to_offset(index_freq)
    
    forecasted_dates = original_df.index[len(original_df) - len(forecasted_values) + 1:]
    forecasted_dates = forecasted_dates.append(pd.DatetimeIndex([next_date]))

    forecasted_df = pd.DataFrame({col_name: forecasted_values}, index=forecasted_dates)

    merged_df = pd.concat([original_df, forecasted_df], axis=1)
    return merged_df