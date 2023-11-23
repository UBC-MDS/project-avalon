from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
import pandas as pd


def get_metrics_from_df(df: pd.DataFrame, observed_column: str, required_metrics: list = ["mae", "mse"]):
    """
    Calculate specified metrics for each forecast column in a DataFrame compared to a target column.
    
    Parameters:
    df (DataFrame): The DataFrame containing the forecasted and actual values.
    observed_column (str): The name of the column in df that contains the actual values.
    required_metrics (list of str): Metrics to calculate. Supported metrics are 'mae', 'mse', and 'mape'.
    
    Returns:
    DataFrame: A DataFrame with the forecast columns and the calculated metrics.
    
    Raises:
    TypeError: If df is not a pandas DataFrame.
    """
    # Check if the df is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "The provided data frame 'df' is not a pandas DataFrame.")

    # Parse the required metrics and check which metrics are needed
    parsed_array = [metr.lower() for metr in required_metrics]
    require_mae = "mae" in parsed_array
    require_mse = "mse" in parsed_array
    require_mape = "mape" in parsed_array

    # Initialize lists to store metric values
    mae_values = [] if require_mae else None
    mse_values = [] if require_mse else None
    mape_values = [] if require_mape else None

    # Calculate metrics for each forecast column compared to the target column
    for col in df.columns[1:]:
        if require_mae:
            mae = mean_absolute_error(df[observed_column], df[col])
            mae_values.append(mae)
        if require_mse:
            mse = mean_squared_error(df[observed_column], df[col])
            mse_values.append(mse)
        if require_mape:
            mape = mean_absolute_percentage_error(df[observed_column], df[col])
            mape_values.append(mape)

    # Prepare a dictionary to create the DataFrame
    results_dict = {'Forecast_Column': df.columns[1:]}
    if require_mae:
        results_dict['MAE'] = mae_values
    if require_mse:
        results_dict['MSE'] = mse_values
    if require_mape:
        results_dict['MAPE'] = mape_values

    # Create a DataFrame to store the results
    results_df = pd.DataFrame(results_dict)

    return results_df
