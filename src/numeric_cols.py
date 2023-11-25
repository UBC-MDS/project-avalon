# author: Mo Norouzi
# date: 2023-11-24

import altair as alt
import pandas as pd

def create_numeric_cols_chart(data, numeric_cols):
    """
    Generates bar charts for numeric columns in a dataset using Altair.

    Parameters:
    ----------
    data : pandas.DataFrame
        The dataset containing the numeric columns.
    numeric_cols : list of str
        The names of the numeric columns to visualize.

    Returns:
    -------
    alt.Chart
        An Altair Chart object displaying the bar charts for the specified numeric columns.

    This function creates a bar chart for each numeric column and combines them into a single Altair Chart.
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

