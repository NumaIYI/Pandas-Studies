import pandas as pd

df = pd.read_csv("nbaabout/Players.csv")

result = df.head()
result = len(df.index)
result = df.columns
print(result)
result = df["height"].mean()
result = df["height"].max()
result = df[df["height"] == df["height"].max()][["Player","height"]]
result = df[df["Player"] == "Manute Bol"]["collage"].iloc[0]
df = df.dropna()

result=len(df.groupby("collage"))
result = df["collage"].nunique()

result = df["collage"].value_counts()

result = df[df["Player"].str.contains("and")]

print(result)