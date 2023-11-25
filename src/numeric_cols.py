# author: Mo Norouzi
# date: 2023-11-24

import altair as alt
import pandas as pd

def create_numeric_cols_chart(data, numeric_cols):
    """
    Generate bar charts for numeric columns in the given dataset.

    Parameters:
    - data (pandas.DataFrame): The dataset containing numeric columns to visualize.
    - numeric_cols (list): List of column names (strings) that are numeric.

    Returns:
    - alt.Chart: Combined Altair chart displaying bar charts for each numeric column.
    """
    alt.data_transformers.enable('vegafusion')
    
    charts = []
    for col in numeric_cols:
        chart = alt.Chart(data).mark_bar().encode(
            alt.X(alt.repeat(), type="quantitative", bin=alt.Bin(maxbins=30)),
            y="count()",
        ).properties(
            width=200,
            height=150
        ).repeat(
            [col],
            columns=2,
        )
        charts.append(chart)
    
    combined_chart = alt.hconcat(*charts)
    return combined_chart

