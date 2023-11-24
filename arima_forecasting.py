def arima_prediction(df, window_size=12):
    """
    Perform ARIMA forecast with a rolling window.

    Parameters:
    -----------
    df : DataFrame
        Input DataFrame containing a single column with a datetime index.
    window_size : int, optional
        Size of the rolling window for forecasting (default=12).

    Returns:
    --------
    list
        A list containing the forecasted values.

    Raises:
    -------
    ValueError
        - If the input DataFrame contains more than one column.
        - If the index of the DataFrame is not a DatetimeIndex.
        - If the only column in the DataFrame is not numerical.
        - If the window size is not a positive integer greater than 1 or exceeds the length of the DataFrame.
    
    Notes:
    ------
    This function takes a DataFrame with a single column and a date index to perform ARIMA prediction.
    It iterates through the DataFrame using a rolling window of 'window_size' length, fits an ARIMA model
    to each window, and forecasts the next value. The function returns a list of forecasted values.
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