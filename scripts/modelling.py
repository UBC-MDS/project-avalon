import click
import os
import numpy as np
import pandas as pd
import pickle
from sklearn import set_config
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import make_column_transformer, make_column_selector
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import fbeta_score, make_scorer

@click.command()
@click.option('--scaled-test-data', type=str, help="Path to scaled test data")
@click.option('--columns-to-drop', type=str, help="Optional: columns to drop")
@click.option('--pipeline-from', type=str, help="Path to directory where the fit pipeline object lives")
@click.option('--results-to', type=str, help="Path to directory where the plot will be written to")
@click.option('--seed', type=int, help="Random seed", default=123)

def main(preprocessed_data , columns_to_drop, pipeline_from, results_to, seed):

    # Define the size of the sliding window
    window_size = 12
    # Define alpha (smoothing parameter in ES)
    alpha=0.3

    # Perform Simple Moving Average (SMA) and Exponential Smoothing (ES)
    sma_values = []
    smoothed_values = []
    for i in range(len(theft_from_vehicle_filtered) - window_size + 1):
        
        window = theft_from_vehicle_filtered['Observations'].iloc[i:i+window_size]

        # SMA
        window_mean = window.mean()
        sma_values.append(window_mean)

        # ES
        smoothed_val = window.ewm(alpha=alpha, adjust=False).mean().iloc[-1]
        smoothed_values.append(smoothed_val)

    sma_merged = merge_forecast_values(theft_from_vehicle_filtered, sma_values, "SMA_Forecast")
    es_merged = merge_forecast_values(theft_from_vehicle_filtered, smoothed_values, "ES_Forecast")

if __name__ == '__main__':
    main()