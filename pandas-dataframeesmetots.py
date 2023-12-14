import numpy as np
import pandas as pd

def kareal(x):
    return x*x

kareal2 = lambda x:x * x

data = {
    "col1" : [1,2,3,4,5],
    "col2" : [10,20,30,40,25],
    "col3" : ["abc","bcaa","cb","daf","cba"]
}
df = pd.DataFrame(data)
result = df["col2"].unique() #tekrarlayanları eliyor yoksa direk devamke
result = df["col2"].nunique() #kaç farklı var bambam
result = df["col2"].value_counts() #kimden kaç tane
result = df["col1"] *2
result = df["col1"].apply(kareal)
result = df["col1"].apply(kareal2)
result = df["col1"].apply(lambda x:x * x)
df["col4"] = df["col3"].apply(len) #guncelleme yabtık ayrıyaten
result = len(df.columns)
result = len(df.index)
result = df.info
result = df.sort_values("col2") # verilen kolona göre sıralama yapıyor
result = df.sort_values("col2",ascending= False) #ters sıralama
df = df.pivot_table(index="col3",columns="col1",values="col2")
print(df)

print(result)