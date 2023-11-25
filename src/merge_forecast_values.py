import pandas as pd

def merge_forecast_values(original_df, forecasted_values, col_name):
    """
    Merge forecasted values into an original DataFrame.

    Parameters:
    -----------
    original_df : DataFrame
        Original DataFrame containing the historical data.
    forecasted_values : array-like
        Forecasted values to be merged into the original DataFrame.
    col_name : str
        Name of the column for the forecasted values.

    Returns:
    --------
    DataFrame
        A new DataFrame with the forecasted values merged into the original data.

    Notes:
    ------
    This function merges the forecasted_values into the original DataFrame,
    assigning them to a new column named col_name. It extracts the frequency
    of the original DataFrame's index to determine the next date, ensuring
    correct alignment of the forecasted values in the merged DataFrame.
    """

    # Check if the original df has more than one column
    if len(original_df.columns) != 1:
        raise ValueError("Input DataFrame must contain only one column for ARIMA prediction.")

    # Check if the index of original df is a DatetimeIndex
    if not isinstance(original_df.index, pd.DatetimeIndex):
        raise ValueError("Index of the DataFrame must be a DatetimeIndex for ARIMA prediction.")

    # Check if the only column in the original df is numerical
    if not pd.api.types.is_numeric_dtype(original_df.iloc[:, 0]):
        raise ValueError("The column in the DataFrame should be numerical for ARIMA prediction.")
    
    # Check if forecasted_values is a list
    if not isinstance(forecasted_values, list):
        raise ValueError("Forecasted values must be a list.")
    
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