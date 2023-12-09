import click
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


@click.command()
@click.option('--prediction_df', type=str, help="Path of predictions csv")
@click.option('--results_folder', type=str, help="Path to results folder")
def main(prediction_df, results_folder):
    data = pd.read_csv(prediction_df, index_col=[0])
    data.index = pd.to_datetime(data.index)

    # Original Plot
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Observations'], label='Original Values', color='black')
    plt.legend()
    plt.title('Original Value')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.savefig(os.path.join(results_folder, "figures", "original_plot.png"))

    # ARIMA Plot
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Observations'], label='Original Values', color='black')
    plt.plot(data.index, data['ARIMA_Forecast'], label='ARIMA Forecasts', color='orange')
    plt.legend()
    plt.title('ARIMA Predictions to Original Value')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.savefig(os.path.join(results_folder, "figures", "arima_prediction_plot.png"))

    # ES Plot
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Observations'], label='Original Values', color='black')
    plt.plot(data.index, data['ES_Forecast'], label='ES Forecasts', color='blue')
    plt.legend()
    plt.title('ES Predictions to Original Value')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.savefig(os.path.join(results_folder, "figures", "es_prediction_plot.png"))

    # SMA Plot
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Observations'], label='Original Values', color='black')
    plt.plot(data.index, data['SMA_Forecast'], label='SMA Forecasts', color='green')
    plt.legend()
    plt.title('SMA Predictions to Original Value')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.savefig(os.path.join(results_folder, "figures", "sma_prediction_plot.png"))


if __name__ == '__main__':
    main()
