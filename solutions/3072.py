import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame `weather` with columns ['city', 'month', 'temperature'],
    pivots it so that each row index is a month (sorted alphabetically),
    each city is a column, and the values are the temperatures.
    """
    # Pivot so that months become the index and cities become columns
    df_pivot = weather.pivot(index='month', columns='city', values='temperature')
    # Sort the months (the index) alphabetically
    df_pivot = df_pivot.sort_index()
    # Sort the city columns alphabetically
    df_pivot = df_pivot[sorted(df_pivot.columns)]
    return df_pivot
