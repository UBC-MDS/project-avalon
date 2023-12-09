import click
import os
import pandas as pd
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.merge_forecast_values import merge_forecast_values
from src.arima_forecasting import arima_prediction


@click.command()
@click.option('--preprocessed_data', type=str, help="Path to preprocessed data")
@click.option('--results_folder', type=str, help="Path to results folder")
def main(preprocessed_data, results_folder):
    data = pd.read_csv(preprocessed_data)
    data = data[['YEAR-MONTH', 'Observations']]
    data.set_index('YEAR-MONTH', inplace=True)
    data.index = pd.to_datetime(data.index)
    print(data)

    # Define the size of the sliding window
    window_size = 12
    # Define alpha (smoothing parameter in ES)
    alpha = 0.3

    # Perform Simple Moving Average (SMA) and Exponential Smoothing (ES)
    sma_values = []
    smoothed_values = []
    for i in range(len(data) - window_size + 1):
        window = data['Observations'].iloc[i:i + window_size]

        # SMA
        window_mean = window.mean()
        sma_values.append(window_mean)

        # ES
        smoothed_val = window.ewm(alpha=alpha, adjust=False).mean().iloc[-1]
        smoothed_values.append(smoothed_val)

    arima_pred_values = arima_prediction(data)

    sma_merged = merge_forecast_values(data, sma_values, "SMA_Forecast")
    es_merged = merge_forecast_values(data, smoothed_values, "ES_Forecast")
    arima_merged = merge_forecast_values(data, arima_pred_values, "ARIMA_Forecast")

    merged_df = pd.concat([sma_merged, es_merged["ES_Forecast"], arima_merged["ARIMA_Forecast"]], axis=1)

    merged_df.to_csv(os.path.join(results_folder, "tables", "all_predictions.csv"))


if __name__ == '__main__':
    main()
