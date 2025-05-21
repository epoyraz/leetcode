import pandas as pd

# Assuming `students` is your DataFrame
def selectData(students, target_id=101):
    """
    Returns a DataFrame containing the name and age of the student
    whose student_id equals target_id.
    """
    return students.loc[students['student_id'] == target_id, ['name', 'age']]