import pandas as pd

data = {
    'Student': ["Amit", "John", "Jacob", "David", "Steve", "Ramesh", "Suresh", ],
    'Rank': [1, 5, 6, 7, 2, 3, 4],
    'Marks': [99, 71, 89, 69, 50, 33, 83]
}

df = pd.DataFrame(data, index = ['RowA', 'RowB', 'RowC', 'RowD', 'RowE', 'RowF', 'RowG'])

print("Student Records\n\n", df)

# Access Using rows and columns by integer positions
print("\nValue = \n", df.iloc[[3,4]])