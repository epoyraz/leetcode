import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    """
    Reshapes the DataFrame from wide to long format so each row represents
    sales for a product in a specific quarter.
    """
    return pd.melt(report, id_vars=['product'], 
                   value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
                   var_name='quarter', value_name='sales')
