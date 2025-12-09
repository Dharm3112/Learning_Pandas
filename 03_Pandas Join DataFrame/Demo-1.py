import pandas as pd

# Dataset
data1 = {
    'id': ["S01", "S02", "S03", "S04", "S05"],
    'student': ["Amit", "John", "Jacob", "David", "Steve"],
    'roll': [101, 102, 103, 104, 105]
}
data2 = {
    'rank': [1, 4, 3, 5, 2],
    'marks': [95, 70, 80, 60, 90]
}

# DataFrame
dataFrame1 = pd.DataFrame(data1)
print("DataFrame1 =\n", dataFrame1)
dataFrame2 = pd.DataFrame(data2)
print("\nDataFrame2 =\n", dataFrame2)

# Join two DataFrames
resDF = dataFrame1.join(dataFrame2)
print("\nJoining DataFrames =\n", resDF)