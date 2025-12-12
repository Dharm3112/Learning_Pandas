import pandas as pd

data1 = [10, 20, 40, 80, 100]
data2 = [25, 5, 75, 95, 45]

series1 = pd.Series(data1)
series2 = pd.Series(data2)

print("Series1:\n", series1)
print("Series2:\n", series2)

def demo (x1, x2):
    if(x1 > x2):
        return x1
    else:
        return x2

    res = series1.combine(series2, demo)

    print("\nAfter combining\n", res)