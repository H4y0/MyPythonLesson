import string
with open("hellowworld.txt","r") as f:
    txt=f.read()
txt = txt.lower()
for x in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
    txt = txt.replace(x, " ") 
lst=txt.split()

d={}
for i in lst:
    d[i]=d.get(i,0)+1
t=list(d.items())
t.sort(key=lambda i:(i[1],i[0]),reverse=True)
print(t[:])