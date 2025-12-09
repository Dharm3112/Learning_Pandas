import pandas as pd

# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100]

# Create a Series using the Series() method
# We have set the Series name using the name attribute
s = pd.Series(data, name="MyNumberSeries")

# Display the Series
print("Series: \n", s)

# Return the name of the Series
print("\nSeries Name: ", s.name)