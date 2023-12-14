import pandas as pd
import numpy as np


data  = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index= ['a','c','e','f','h'], columns=["col1","col2","col3"])

df = df.reindex(['a','b','c','d','e','f','g','h'])
newCol = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["col4"] = newCol
result = df
result = df.drop("col1",axis=1)
result = df.drop(["col1","col2"],axis=1)
result = df.drop('a',axis=0)
result = df.drop(['a','b','h'],axis= 0)
result = df.isnull()
result = df.notnull()
result = df.isnull().sum()
result = df["col1"].isnull().sum()
result = df[df["col1"].notnull()][["col1","col2"]]
result = df.dropna(axis=1)
result = df.dropna(how="any")
result = df.dropna(how="all")
result = df.dropna(subset= ["col1","col2"],how="all")
result = df.dropna(subset= ["col1","col2"],how="all")
result = df.dropna(thresh= 3) # en az sayıda normal veri
result = df.fillna(value= 'no inputtee') #nan ların yerine istediini koyuyor
result = df.sum().sum()
result = df.size
result = df.isnull().sum().sum()

def ortalama(df):
    total = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return total / adet

result = df.fillna(value=ortalama(df))

print(result)
