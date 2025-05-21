import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    """
    Given a DataFrame employees with columns ['name', 'salary'],
    modifies the DataFrame in-place so that each salary is doubled,
    and returns it.
    """
    employees['salary'] = employees['salary'] * 2
    return employees
