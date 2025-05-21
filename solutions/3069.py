import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame students with a float 'grade' column,
    converts 'grade' to integer type and returns the DataFrame.
    """
    students['grade'] = students['grade'].astype(int)
    return students
