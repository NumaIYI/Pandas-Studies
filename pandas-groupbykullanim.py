import pandas as pd

personeller = {
    "çalışan" : ["ahmed","can","hasan","cenk","ali","zeynep","fatma"],
    "departman": ["insan kaynakları","bilgi işlem","muhasebe","insan kaynakları","insan kaynakları","muhasebe","bilgi işlem"],
    "yaş" : [30,25,45,50,23,34,42],
    "semt" : ["kadıköy","maltepe","kadıköy","tuzla","kadıköy","maltepe","kadıköy"],
    "maaş" : [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)

result = df
result = df["maaş"].sum()
result = df.groupby(["departman","semt"]).groups
print(result)
'''
semtler = df.groupby("semt")

for name,group in semtler:
    print(name)
    print(group)
    #semtleri aynı olanları sırayla yazdı'''

result = df.groupby("semt").get_group("kadıköy")

print(result)