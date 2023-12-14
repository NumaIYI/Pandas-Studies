import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index= ["A","B","C"],columns=["col1","col2","col3"])
result = df
result = df[["col1","col2"]] #iki kolu aldık 
result = df.loc["A"] #A satırı
result =df.loc[:,["col1","col2"]] 
result = df.loc[:,"col1":"col3"] #col1-col3 dahil aradaki hepi
result = df.loc["A":"B",:"col2"]
result = df.iloc[2] #indexe göre alıyor isimliyse bile 
result = df.loc["A","col1"]
df["col4"] = pd.Series(randn(3),["A","B","C"])

print(result)
print(df.drop("col4",axis=1)) #axis bir yukardan aşşağıya


print(df)
