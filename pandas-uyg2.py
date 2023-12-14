import pandas as pd

df = pd.read_csv("GBvideos.csv")
result = df.head(10)
result = df[5:20].head()
result = df.columns
df = df.drop([ 'thumbnail_link', 'trending_date' , 'comments_disabled', 'ratings_disabled','video_error_or_removed', 'description'],axis=1)
result = df
result = df[["likes","dislikes"]].mean()
result = df[["likes","dislikes"]].head(50)
result = df[ (df["views"].max()) == df['views']]["title"]
result = df[ (df["views"].min()) == df['views']]["title"]
result = df.sort_values("views",ascending= False).head(10)[["title","views"]]
result = df.groupby("category_id")["likes"].mean().sort_values()
result = df.groupby("category_id")["comment_count"].sum().sort_values(ascending=False)
result = df.groupby("category_id").count()["video_id"].sort_values(ascending=False)
#df["lenght_of_title"] = len(str(df["title"]))
df["lenght_of_title"] = df["title"].apply(len)
result = df
df["tag_sayisi"] = df["tags"].apply(lambda x: len(x.split('|')))
result = df

#result = df[df["likes"] - df["dislikes"]].sort_values(ascending=False)
likelist = list(df["likes"])
dislikelist = list(df["dislikes"])

def oranhesab(dataset):
    likelist = list(dataset["likes"])
    dislikelist = list(dataset["dislikes"])

    liste = list(zip(likelist,dislikelist))

    oranlistesi = []

    for i,j in liste:
       if(i+j) == 0:
           oranlistesi.append(0)
       else:
           oranlistesi.append(i/(i+j))

    return oranlistesi              





'''['video_id', 'trending_date', 'title', 'channel_title', 'category_id',
       'publish_time', 'tags', 'views', 'likes', 'dislikes', 'comment_count',
       'thumbnail_link', 'comments_disabled', 'ratings_disabled',
       'video_error_or_removed', 'description']'''
df["begeni_orani"] = oranhesab(df)
print(df.sort_values("begeni_orani",ascending=False)[["title","likes","dislikes","begeni_orani"]].head())