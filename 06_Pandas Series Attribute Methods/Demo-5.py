import pandas as pd
import numpy as np

# Data to be stored in the Pandas Series
data = [10, 20, 40, 80, 100, np.NaN]

# Create a Series using the Series() method
s = pd.Series(data)

# Display the Series
print("Series: \n", s)

# Check whether the Series has NaNs
print("\nDoes the Series has NaN? ", s.hasnans)