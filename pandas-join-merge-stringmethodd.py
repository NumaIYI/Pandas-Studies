import pandas as pd

'''data = pd.read_csv("imdb250.csv")

data.dropna(inplace=True)
result = data.columns
print(data.head()["name"])
data["name"] = data["name"].str.upper()
print(data.head()["name"])'''
#***********************************************************************
#*************************************************************
#***********************************************************************

'''customers = {
    'customerId' : [1,2,3,4],
    'firstName': ["ahmet","ali","hasan","canan"],
    'lastname':["yilmaz","korkmaz","celik","toprak"]
}

orders = {
    'orderId' : [10,11,12,13],
    'customerId':[1,2,5,7],
    'orderDate':["2010-07-04","2010-06-04","2010-08-04","2012-07-04"]
}

df_costumers = pd.DataFrame(customers,columns=["customerId","firstName","lastname"])
df_oeders = pd.DataFrame(orders,columns=["orderId","customerId","orderDate"])

print(df_costumers)
print(df_oeders)

result = pd.merge(df_costumers,df_oeders,how="inner")

result = pd.merge(df_costumers,df_oeders,how="left")

result = pd.merge(df_costumers,df_oeders,how="right")

result = pd.merge(df_costumers,df_oeders,how="outer") '''

customerA = {
    'customerId' : [1,2,3,4],
    'firstName': ["ahmet","ali","hasan","canan"],
    'lastname':["yilmaz","korkmaz","celik","toprak"]
}

customerB = {
    'customerId' : [4,5,6,7],
    'firstName': ["ayu","veli","hüseyin","hagan"],
    'lastname':["kırmaz","ortar","comak","ateş"]
}

df_cA = pd.DataFrame(customerA,columns=["customerId","firstName","lastname"])
df_cB = pd.DataFrame(customerB,columns=["customerId","firstName","lastname"])

result = pd.concat([df_cA,df_cB])

print(result)