from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
import pandas as pd


def get_metrics_from_df(df, observation_column: str, required_metrics: list = ["mae", "mse"]):
    """
    Calculates specified metrics comparing forecasted values to actual observations in a DataFrame.

    Parameters:
    ----------
    df : pandas.DataFrame
        The DataFrame with actual and forecasted values.
    observation_column : str
        The name of the column containing actual values.
    required_metrics : list of str
        The metrics to calculate, supported: 'mae', 'mse', 'mape'.

    Returns:
    -------
    pandas.DataFrame
        A DataFrame with the calculated metrics for each forecast column.

    This function computes the Mean Absolute Error (MAE), Mean Squared Error (MSE), and Mean Absolute Percentage Error (MAPE)
    for forecast columns compared to the observation column and returns a summary DataFrame.
    """
    # Check if the df is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "The provided data frame 'df' is not a pandas DataFrame.")

    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The provided DataFrame 'df' is empty.")

    # Check if the observation column is in the DataFrame
    if observation_column not in df.columns:
        raise KeyError(
            f"The observation column '{observation_column}' is not in the DataFrame.")

    # Parse the required metrics and check which metrics are needed
    parsed_array = [metr.lower() for metr in required_metrics]
    require_mae = "mae" in parsed_array
    require_mse = "mse" in parsed_array
    require_mape = "mape" in parsed_array

    # Initialize lists to store metric values
    mae_values = [] if require_mae else None
    mse_values = [] if require_mse else None
    mape_values = [] if require_mape else None

    # Calculate metrics for each forecast column compared to the observation column
    for col in df.columns:
        if col != observation_column:
            if require_mae:
                mae = mean_absolute_error(df[observation_column], df[col])
                mae_values.append(mae)
            if require_mse:
                mse = mean_squared_error(df[observation_column], df[col])
                mse_values.append(mse)
            if require_mape:
                mape = mean_absolute_percentage_error(
                    df[observation_column], df[col])
                mape_values.append(mape)

    # Prepare a dictionary to create the DataFrame
    results_dict = {'Forecast_Column': [
        col for col in df.columns if col != observation_column]}
    if require_mae:
        results_dict['MAE'] = mae_values
    if require_mse:
        results_dict['MSE'] = mse_values
    if require_mape:
        results_dict['MAPE'] = mape_values

    # Create a DataFrame to store the results
    results_df = pd.DataFrame(results_dict)

    return results_df
