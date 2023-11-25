import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def arima_prediction(df, window_size=12):
    """
    Performs an ARIMA forecast using a rolling window approach.

    Parameters:
    ----------
    df : pandas.DataFrame
        The input DataFrame must contain a single column with a datetime index.
    window_size : int, optional
        The size of the rolling window for the forecast (default is 12).

    Returns:
    -------
    list
        A list containing the forecasted values for each window.

    Raises:
    ------
    ValueError
        If the DataFrame does not meet the requirements specified in the docstring.

    Notes:
    -----
    The function fits an ARIMA model to each window of the specified size and forecasts
    the next value. The DataFrame index is adjusted for inferred frequency to align the forecasted values.
    """

    # Check if the input DataFrame has more than one column
    if len(df.columns) != 1:
        raise ValueError("Input DataFrame must contain only one column for ARIMA prediction.")

    # Check if the index is a DatetimeIndex
    if not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("Index of the DataFrame must be a DatetimeIndex for ARIMA prediction.")

    # Check if the only column in the DataFrame is numerical
    if not pd.api.types.is_numeric_dtype(df.iloc[:, 0]):
        raise ValueError("The column in the DataFrame should be numerical for ARIMA prediction.")

    # Check if the window_size is a valid integer
    if not isinstance(window_size, int) or window_size <= 1 or window_size > len(df):
        raise ValueError("Window size must be a positive integer that is greater than 1 and less than the length of df for ARIMA prediction.")
        
    # Adjust dataframe index inferred frequency
    df.index = pd.DatetimeIndex(df.index.values, freq=df.index.inferred_freq)

    # Perform ARIMA forecast with a rolling window
    forecasted_values = []
    for i in range(len(df) - window_size + 1):

        window = df.iloc[i:i+window_size+1, 0]
        
        model = ARIMA(window, order=(1, 1, 0))
        model_fit = model.fit()
        
        next_value = model_fit.forecast(steps=1).item()
        forecasted_values.append(next_value)

    return forecasted_values