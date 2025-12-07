import pandas as pd

# Dataset
data = {
    'Student': ["Amit", "John", "Jacob", "David", "Steve", "Ramesh", "Suresh", ],
    'Rank': [1, 2, 3, 4, 5, 6, 7],
    'Marks': [99, 71, 89, 69, 50, 33, 83]
}

# Index Arguments to set your indexes
df = pd.DataFrame(data, index = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7'])

print("Student Records\n\n", df)

# Iterationg
print("\nDisplay Columns : ")

for col in df:
    print(col)