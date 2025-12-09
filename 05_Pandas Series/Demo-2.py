import pandas as pd

# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100]

# Create a Series using the Series() method
s = pd.Series(data)

# Display the Series
print("Series: \n", s)

# Access a value
print("\nValue from a Pandas Series: ", s[2])