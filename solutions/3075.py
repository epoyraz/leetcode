import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame students with columns ['student_id', 'name', 'age'],
    returns a new DataFrame with any rows removed where 'name' is missing (NaN or None).
    """
    return students.dropna(subset=['name'])
