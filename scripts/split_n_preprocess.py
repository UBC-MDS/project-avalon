# split_n_preprocess.py
# author: Yiwei Zhang
# date: 2023-12-01

import click
import sys
import os
import numpy as np
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.capture_df_info import capture_df_info


@click.command()
@click.option('--raw-data', type=str, help="Path to raw data")
@click.option('--data-to', type=str, help="Path to directory where processed data csv will be written to")
@click.option('--preview_to', type=str, help="Path to directory where the preview csv will be written to")
# python3 split_n_preprocess.py "../data/crimedata_csv_AllNeighbourhoods_AllYears.csv" "../reports"

def main(raw_data, data_to, preview_to=None):
    """
    Main function that handles reading the raw CSV data, preprocessing it, and writing the output.

    Parameters:
    raw_data (str): Path to the raw data CSV file.
    data_to (str): Path to directory where processed data will be written to.
    preview_to (str, optional): Path to directory where a preview of the processed data will be written to.
                                Defaults to the same path as 'data_to' if not specified.
    """
    if raw_data is None:
        raw_data = "../data/raw/crimedata_csv_AllNeighbourhoods_AllYears.csv"

    if data_to is None:
        data_to = "../data/processed"

    if preview_to is None:
        preview_to = data_to

    df = pd.read_csv(raw_data, encoding="utf-8")
    # df = pd.read_csv(raw_data, header=None).drop(columns=['id'])

    data_general_full_path = os.path.join(data_to, "preprocessed_data_full.csv")
    data_general_head_path = os.path.join(preview_to, "preprocessed_data_head.csv")

    # Group by the dataset to find the number of observations for each crime in a specific month
    grouped = df.groupby(['TYPE', 'YEAR', 'MONTH']).size().reset_index(name='Observations')
    # Combine YEAR and MONTH into a datetime variable
    grouped['YEAR-MONTH'] = pd.to_datetime(grouped[['YEAR', 'MONTH']].assign(DAY=1))
    # Remove rows with time 2023-11 because the data is incomplete
    grouped = grouped[~((grouped['YEAR'] == 2023) & (grouped['MONTH'] == 11))]

    grouped.to_csv(data_general_full_path, index=False)
    grouped.head().to_csv(data_general_head_path, index=False)

    data_theft_from_vehicle_full_path = os.path.join(data_to, "preprocessed_theft_from_vehicle_full.csv")
    data_theft_from_vehicle_head_path = os.path.join(preview_to, "preprocessed_theft_from_vehicle_head.csv")
    data_theft_from_vehicle_info_path = os.path.join(preview_to, "preprocessed_theft_from_vehicle_info.txt")

    # Store the specified column to CSV
    theft_from_vehicle = grouped[grouped['TYPE'] == 'Theft from Vehicle']

    theft_from_vehicle.to_csv(data_theft_from_vehicle_full_path, index=False)
    theft_from_vehicle.head().to_csv(data_theft_from_vehicle_head_path, index=False)

    # Capture the DataFrame info and write to a file
    info = capture_df_info(theft_from_vehicle)
    with open(data_theft_from_vehicle_info_path, "w") as f:
        f.write(info)


if __name__ == '__main__':
    main()
