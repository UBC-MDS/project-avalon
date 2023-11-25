import pandas as pd


def get_redundant_pairs(df):
    """
    Identify redundant pairs of columns in a DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.

    Returns
    -------
    set
        A set containing pairs of column names that are redundant.

    Raises
    ------
    TypeError
        If the input 'df' is not a pandas DataFrame.

    Notes
    -----
    Redundant pairs include both (A, B) and (B, A), where A and B are column names.
    This function is used to retain only one pair as correlation is not directional.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "The provided data frame 'df' is not a pandas DataFrame.")

    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop


def get_top_abs_correlations(df, n=5):
    """
    Get the top absolute correlations in a DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame for which correlations need to be calculated.
    n : int, optional
        The number of top correlations to retrieve. Default is 5.

    Returns
    -------
    pandas.Series
        A pandas Series containing the top absolute correlations, sorted in descending order.

    Raises
    ------
    TypeError
        If the input 'df' is not a pandas DataFrame.

    Examples
    --------
    >>> correlations = get_top_abs_correlations(my_dataframe, 3)
    >>> print(correlations)
    column1  column2    0.95
    column3  column4    0.87
    column2  column5    0.78
    dtype: float64
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(
            "The provided data frame 'df' is not a pandas DataFrame.")

    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]
