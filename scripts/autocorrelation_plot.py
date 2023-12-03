import click
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


@click.command()
@click.option('--preprocessed_data', type=str, help="Path to preprocessed data")
@click.option('--results_folder', type=str, help="Path to results folder")
def main(preprocessed_data, results_folder):
    data = pd.read_csv(preprocessed_data)
    data = data[['YEAR-MONTH', 'Observations']]
    data.set_index('YEAR-MONTH', inplace=True)
    data.index = pd.to_datetime(data.index)

    # Autocorrelation Plot
    autocorrelation_plot(data.Observations)
    plt.savefig(os.path.join(results_folder, "figures", "autocorrelation_plot.png"))
    plt.clf()

    # Autocorrelation Plot with diff=1
    data_diff = data.diff().dropna()
    autocorrelation_plot(data_diff.Observations)
    plt.savefig(os.path.join(results_folder, "figures", "autocorrelation_with_diff_plot.png"))


if __name__ == '__main__':
    main()
