import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Given two DataFrames `df1` and `df2` with the same columns,
    returns a single DataFrame with `df2`'s rows appended below `df1`'s rows.
    """
    return pd.concat([df1, df2], ignore_index=True)
