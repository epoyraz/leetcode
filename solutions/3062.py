import pandas as pd

def createDataframe(student_data):
    """
    Given a 2D list student_data where each sublist is [student_id, age],
    returns a pandas DataFrame with columns ['student_id', 'age'] in the same order.
    """
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df
