import pandas as pd

# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100]

# Create a Series using the Series() method
s = pd.Series(data, index=["RowA", "RowB", "RowC", "RowD", "RowE"])

# Display the Series
print("Series (with custom index labels): \n", s)

# Access a value referring the lable
print("\nValue from a Pandas Series with label RowD: ", s["RowD"])