import pandas as pd

# Assuming `players` is your DataFrame
def getDataframeSize(df):
    """
    Returns the number of rows and columns of the DataFrame as a list: [n_rows, n_columns].
    """
    return list(df.shape)