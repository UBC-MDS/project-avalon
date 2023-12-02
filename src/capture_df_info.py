# Additional import for function extraction
from io import StringIO

def capture_df_info(dataframe):
    """
    Captures the info of the specified pandas DataFrame into a string.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame for which info is to be captured.

    Returns:
    str: Info about the DataFrame as a string.
    """
    buffer = StringIO()
    dataframe.info(buf=buffer)
    return buffer.getvalue()
