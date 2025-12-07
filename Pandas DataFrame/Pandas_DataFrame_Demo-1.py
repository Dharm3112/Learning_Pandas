import pandas as pd

#Dataset
data = {
    'Student' : ["Amit","John","Jacob","David","Steve","Ramesh","Suresh",],
    'rank' : [1,2,3,4,5,6,7],
    'marks' : [99,71,89,69,50,33,83]
}

df = pd.DataFrame(data)

print("Student ecords\n\n", df)
