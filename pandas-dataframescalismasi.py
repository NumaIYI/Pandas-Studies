import pandas as pd
import numpy as np

data = [["ahmed",50],["ali",60],["yagmur",70],["cinar",80]]
dct1 = {"name":["hakan","hulusi","yunus","emir"],"grade":[50,60,70,80]}
dct_lst = [{"name":"hakan","grade":50},
           {"name":"hulusi","grade":60},
           {"name":"yunus","grade":70},
           {"name":"emir","grade":80}
           ]
#df = pd.DataFrame(data, index = [1,2,3,4], columns = ['Name','Grade'], dtype=float) #bişi yazmassan sıralam aynı olur.

df = pd.DataFrame(dct1)
df = pd.DataFrame(dct1,index=["212","232","236","435"])
df = pd.DataFrame(dct_lst,index=["212","232","236","435"])
print(df)


'''s1 = pd.Series([3,2,1,0])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1, oranges = s2)

df = pd.DataFrame(data)
print(df)'''