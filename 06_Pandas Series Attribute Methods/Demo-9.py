import pandas as pd

# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100, 200, 300, 500]

# Create a Series using the Series() method
s = pd.Series(data, index=["RowA", "RowB", "RowC", "RowD", "RowE", "RowF", "RowG", "RowH"])

# Display the Series
print("Series (with custom index labels): \n", s)

# Return the summary of the series
print("\nSeries Summary:\n", s.info())
