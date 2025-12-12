import pandas as pd

df = pd.DataFrame(
    data={"Cat1": list("pqrs"),
          "Cat2": list("pqrp"),
          "Cat3": list("qrrr")},
    dtype="category"
)

print("DataFrame = \n", df)

print("\nDatatypes of each column = \n", df.dtypes)