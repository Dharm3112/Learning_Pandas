import pandas as pd

# Dataset

data = {
    'Student': ["Amit", "John", "Jacob", "David", "Steve", "Ramesh", "Suresh", ],
    'Rank': [1, 2, 3, 4, 5, 6, 7],
    'Marks': [99, 71, 89, 69, 50, 33, 83]
}

df = pd.DataFrame(data, index = ['RowA', 'RowB', 'RowC', 'RowD', 'RowE', 'RowF', 'RowG'])

print("Student Records\n\n", df)

# Access the value in student column corresponding to RowA label
print("\nValue = ", df.loc['RowA', 'Student'])
