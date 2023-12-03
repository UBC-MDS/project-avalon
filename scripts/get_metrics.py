import os
import sys

import click
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.get_metrics_from_df import get_metrics_from_df


@click.command()
@click.option('--predictions_data', type=str, help="Path to the CSV file containing the prediction data")
@click.option('--results_folder', type=str, help="Path to results folder")
def main(predictions_data, results_folder):
    predictions = pd.read_csv(predictions_data, index_col=0)
    predictions_drop_na = predictions.dropna()

    results_df = get_metrics_from_df(predictions_drop_na, "Observations")

    results_df.to_csv(os.path.join(results_folder, "tables", "observations.csv"))


if __name__ == '__main__':
    main()
