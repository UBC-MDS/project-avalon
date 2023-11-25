# author: Mo Norouzi
# date: 2023-11-24

def missing_zero_values_table(df):
    """
    Generate a summary table that identifies the count and percentage of missing values
    and zero values in the provided DataFrame.

    Parameters:
    - df (pandas.DataFrame): The DataFrame for which missing and zero values are to be analyzed.

    Returns:
    - pandas.DataFrame: A table displaying the count and percentage of zero values,
      missing values, their combined total, percentage of the total values, and the data types
      of the columns containing these values.
      
    The table is sorted in descending order based on the percentage of missing or zero values.

    Example Usage:
    ```
    # Assuming 'data' is your dataset
    missing_zero_values_table(data)
    ```
    """
    zero_val = (df == 0.00).astype(int).sum(axis=0)
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    mz_table = pd.concat([zero_val, mis_val, mis_val_percent], axis=1)
    mz_table = mz_table.rename(
    columns = {0 : 'Zero Values', 1 : 'Missing Values', 2 : '% of Total Values'})
    mz_table['Total Zero Missing Values'] = mz_table['Zero Values'] + mz_table['Missing Values']
    mz_table['% Total Zero Missing Values'] = 100 * mz_table['Total Zero Missing Values'] / len(df)
    mz_table['Data Type'] = df.dtypes
    mz_table = mz_table[
        mz_table.iloc[:,1] != 0].sort_values(
    '% of Total Values', ascending=False).round(1)
    print ("Your selected dataframe has " + str(df.shape[1]) + " columns and " + str(df.shape[0]) + " Rows.\n"      
           "There are " + str(mz_table.shape[0]) +
              " columns that have missing values.")
    return mz_table
missing_zero_values_table(data)