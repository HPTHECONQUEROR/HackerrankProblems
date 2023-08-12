p=input("ENTER PHONE NUMBER : ")
n={"1":'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','0':'zero'}
o=""
for m in p:
    o+=n.get(m,'1') + ""
print(o)