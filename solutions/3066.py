import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame employees with columns ['name', 'salary'],
    returns the DataFrame with an added 'bonus' column equal to 2 * salary.
    """
    employees['bonus'] = employees['salary'] * 2
    return employees
