import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame products with columns ['name', 'quantity', 'price'],
    fills missing values in 'quantity' with 0 and returns the DataFrame.
    """
    products['quantity'] = products['quantity'].fillna(0).astype(int)
    return products
