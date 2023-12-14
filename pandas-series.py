import pandas as pd
import numpy as np

numbers = [20,30,40,50]
letters = ['a','b','c',20,"abc"]
#scalar = 5 
#pandas_series = pd.Series(scalar,[1,2,3,4])
dict1 = {'a':10,'b':20,'c':30,'d':50}
randnums = np.random.randint(10,100,6)
pandas_series = pd.Series(numbers,['a','b','c','d'])
pandas_series = pd.Series(randnums)
result = pandas_series[0]
result = pandas_series[-2:]

#print(pandas_series)

#print(pandas_series.ndim)

opel2018 = pd.Series([20,30,40,50],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([20,30,40,50],["astra","corsa","Grandland","insignia"])

total = opel2018 +opel2019
print(total)