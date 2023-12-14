import pandas as pd

df = pd.read_excel("2022Lgs.xlsx")
#bize gelen bu belge çok karışık bir şekilde aralarda saçma sapan yazılarla dolu ve eksik geldi.
result = df
result = df.columns
df = df[(df['Unnamed: 0']) != "Tercih Kodu"] 
df = df.rename(columns={"Unnamed: 0":"Tercih Kodu", "Unnamed: 1":"İl","Unnamed: 2":"İlçe","Unnamed: 3":"Okul Adı","Unnamed: 4":"Alan Adı","Unnamed: 5":"Süresi","(twitter/unsalim)":"Öğr şekli","Unnamed: 7":"Pansiyon","Unnamed: 8":"Y.dil","2022 LGS":"2022 Yüzde dilimi","Unnamed: 11":"silin","Kontenjan Bilgileri":"2023 Kont","Unnamed: 13":"2022 Kont","Unnamed: 14":"silin2","Unnamed: 16":"Dilim etkisi"},inplace=False) #kafa karışıklığına sebep veren kolon isimlerinin değiştirilmesi 
df = df.drop(["silin","silin2",'Unnamed: 9'],axis=1,inplace=False) #gereksiz 2 kolonun silinmesi

result = df[(df['2022 Yüzde dilimi']) != "**" ] #burada yazı ile aralara sıkışmış ** yazılarının dışındaki satırları aldım
result = result[((result['2022 Yüzde dilimi']) != "2022 LGS")]  #burada yazı ile aralara sıkışmış 2022 LGS yazılarının dışındaki satırları aldım
result = result[((result["Pansiyon"]) == "Kız") | ((result["Pansiyon"]) == "Kız+Erk.")] #burada kardeşim kız olduğu için sadece Kız yurdu olan ve Kız+erkek yurdu olanları aldım
result = result.sort_values('2022 Yüzde dilimi')[["Okul Adı","2022 Yüzde dilimi","Pansiyon","Alan Adı","Tercih Kodu"]].head(40)  #ayırma ve seçme işlemleri sonunda yüzdelik dilim kolonunda sadece float type kalması üzerine sıralama yapılabilir hale geldi. Biz de bu sayede o kolona göre sıralama yapabildik
print(result)
