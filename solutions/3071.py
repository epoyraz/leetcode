import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame customers with columns ['customer_id', 'name', 'email'],
    returns a new DataFrame with duplicate emails dropped, keeping only the first occurrence.
    """
    return customers.drop_duplicates(subset=['email'], keep='first')
