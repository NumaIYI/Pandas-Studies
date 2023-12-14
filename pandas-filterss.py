import numpy as np
import pandas as pd
data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns=["col1","col2","col3","col4","col5"])

result = df
result =df.columns
result = df.head(10)
result = df.tail(5)
result = df["col1"].head()
result = df.col1.head()
result = df[["col1","col2"]].head()
result = df[5:15][["col1","col2"]].head()
result = df > 50
result = df[df>50]
result = df[df["col1"]%2==0][["col1","col2"]]  #col1 i 2 ye bölenleri olan satırları aldı üstüne sadece iki kolon olmak istedik .
result = df[(df["col1"]>50) & (df["col1"]<=75)][["col1","col3"]]
result = df[(df["col1"]>50) | (df["col2"]<=75)] #veya operatörü
result = df.query("col1 >= 50 & col1 % 2 == 0")
print(result) 