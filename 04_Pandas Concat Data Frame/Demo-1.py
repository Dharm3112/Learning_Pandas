import pandas as pd

# Dataset
data1 = {
    'id': ["S01", "S02", "S03", "S04", "S05"],
    'student': ["Amit", "John", "Jacob", "David", "Steve"],
    'roll': [101, 102, 103, 104, 105]
}
data2 = {
    'id': ["S06", "S07", "S08"],
    'student': ["Ben", "Kane", "Rohit"],
    'roll': [106, 107, 108]
}

# DataFrame
dataFrame1 = pd.DataFrame(data1, index=[0, 1, 2, 3, 4])
print("DataFrame1 =\n", dataFrame1)
dataFrame2 = pd.DataFrame(data2, index=[5, 6, 7])
print("\nDataFrame2 =\n", dataFrame2)

# Concatenating two DataFrames
resDF = pd.concat([dataFrame1, dataFrame2])
print("\nConcatenating DataFrames =\n", resDF)