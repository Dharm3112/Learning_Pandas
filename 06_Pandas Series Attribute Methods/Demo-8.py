import pandas as pd

# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100, 200, 300, 500]

# Create a Series using the Series() method
s = pd.Series(data, index=["RowA", "RowB", "RowC", "RowD", "RowE", "RowF", "RowG", "RowH"])

# Display the Series
print("Series (with custom index labels): \n", s)

# Return the last n rows.
# The 5 is default for n
print("\nThe last 5 rows of the series:\n", s.tail())