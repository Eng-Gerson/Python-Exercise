import pandas as pd
import matplotlib.pyplot as plt
results = pd.DataFrame({
    "student": ["Alice", "Bob", "Carol", "David"],
    "python_score": [8, 5, 9, 6],
    "math_score": [7, 6, 8, 5]
})

print(results)
#Complete the following tasks:
#1. Select only the `student` and `python_score` columns.
#2. Define a function called `classify_result` that returns `"Passed"` for scores greater than or equal to 6 and `"Failed"` otherwise.
#3. Use a loop to print the name of each student and the corresponding classification.
#4. Create a bar chart showing the Python score of each student.
