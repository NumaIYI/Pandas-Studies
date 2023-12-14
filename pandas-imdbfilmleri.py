import pandas as pd
df = pd.read_csv("imdb250.csv")
'''['rank', 'name', 'year', 'rating', 'genre', 'certificate', 'run_time',
       'tagline', 'budget', 'box_office', 'casts', 'directors', 'writers']'''
result = df
result = df.columns
result = df.head(10)
result = df.tail(10)
result = df["name"].head(15)
result = df[["name","rating"]].head(15)
result = df[5:][["name","rating"]].head(10)
result = df[df["rating"]>=8.5][["name","rating"]].head(50)
result = df[(df["year"] >= 2014) & (df["year"] <= 2015)][["name","year"]]
#result = df[(df["budget"] > 100000) & ((df["rating"] >= 8) & (df["rating"] <= 9))]

print(result)
